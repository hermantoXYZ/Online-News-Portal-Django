from django.shortcuts import render, redirect, get_object_or_404
from blog.models import Post, Kategori
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
import random
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from taggit.models import Tag
from django.template.context import RequestContext
from django.db.models import Q
# Create your views here.

def PostList(request):
    kategori = Kategori.objects.all()
    queryset = Post.objects.filter(status=1).order_by('-created_on').select_related('kategori')
    randompost = random.sample(list(queryset), min(len(queryset),4))
    # query_set = Post.objects.filter(id__in=randompost)
    # print(queryset)
    for x in queryset:
        print(x.kategori)
    paginator = Paginator(queryset, 10)  # 3 posts in each page
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
            # If page is not an integer deliver the first page
        post_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        post_list = paginator.page(paginator.num_pages)
    data = {
        'data':queryset,
        'page':page,
        'post_list': post_list,
        'randompost':randompost,
        'kategori':kategori
    }
    # print(page)
    # print(post_list)
    # if request.GET.get('amp', 0) == 1:
    #     return render(request,"blog/index.html",data)    
    # else:
    #     return HttpResponse(request.GET.get('amp', 0)) 
    return render(request,"amp_blog/index.html",data) 


def tagged(request, slug):
    kategori = Kategori.objects.all()
    tag = get_object_or_404(Tag, slug=slug)
    # Filter posts by tag name  
    posts = Post.objects.filter(tags=tag,status=1)
    queryset = Post.objects.all().filter(status=1)
    randompost = random.sample(list(queryset), min(len(queryset),4))
    
    paginator = Paginator(posts, 10)  # 3 posts in each page
    page = request.GET.get('page')
    # q = request.GET.get('q')

    # print(ht)
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
            # If page is not an integer deliver the first page
        post_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        post_list = paginator.page(paginator.num_pages)
    
    context = {
        'slug':slug,
        'hitung':posts.count(),
        'tag':tag,
        'post_list':post_list,
        'randompost':randompost,
        'kategori':kategori,
        'page':page,
    }
    # for x in posts:
        # print(x.created_on)
    return render(request, 'amp_blog/tag.html', context)

def KategoriShow(request, slug):
    dt = Post.objects.all().select_related('kategori').filter(status=1,kategori__kategori__contains=slug)
    # for x in dt:
        # print(x)
    # dt = Kategori.objects.all().filter(kategori__contains=slug)
    kategori = Kategori.objects.all()
    namakategori = Kategori.objects.all().filter(kategori__contains=slug).first()
    queryset = Post.objects.all().filter(status=1)
    randompost = random.sample(list(queryset), min(len(queryset),4))
    
    paginator = Paginator(dt, 10)  # 3 posts in each page
    page = request.GET.get('page')
    # q = request.GET.get('q')

    # print(ht)
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
            # If page is not an integer deliver the first page
        post_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        post_list = paginator.page(paginator.num_pages)
    
    data = {
        'namakategori':namakategori,
        'hitung':dt.count(),
        'slug':slug,
        'post':dt,
        'randompost':randompost,
        'kategori':kategori,
        'page':page,
        'post_list': post_list,
    }
    return render(request,"amp_blog/kategori.html",data)

def PostDetail(request, slug):
    dt = Post.objects.filter(status=1).select_related('kategori').get(slug=slug)
    # print(dt.slug)
    kategori = Kategori.objects.all()
    queryset = Post.objects.all().filter(status=1)
    randompost = random.sample(list(queryset), min(len(queryset),4))
    data = {
        'post':dt,
        'randompost':randompost,
        'kategori':kategori
    }
    return render(request,"amp_blog/detailpost.html",data)