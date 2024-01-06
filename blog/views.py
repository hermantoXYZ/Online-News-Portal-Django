from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Kategori, Iklan, StaticPage
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
import random
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from taggit.models import Tag
from django.template.context import RequestContext
from django.db.models import Q
from csp.decorators import csp_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import * 
from rest_framework.views import APIView
from rest_framework import viewsets, status
from django.utils import timezone
from django.views.generic.detail import DetailView, View


class StaticPageView(DetailView):
    model = StaticPage
    template_name = 'blog/static_page.html'
    context_object_name = 'static_page'

class ListViewSet(APIView):
    def get(self, request):
        datanya = Post.objects.filter(status=1).all()
        serializer = ArticleSerializer(datanya, many=True)
        return Response(serializer.data)
    
class IndexView(View):
    template_name = 'blog/indeks.html'  # Replace with the actual template name

    def get(self, request, *args, **kwargs):
        kategori = Kategori.objects.all()
        now = timezone.now()
        queryset = Post.objects.filter(Q(status=1, publish_date__lte=now) | Q(status=2, publish_date__lte=now)).order_by('-created_on').select_related('kategori')
        randompost = random.sample(list(queryset), min(len(queryset), 10))
        popular_posts = Post.objects.filter(status=1).order_by('-views')[:6]

        # Menambahkan definisi latest_headline
        headline_list = Post.objects.filter(is_headline=True, status=1)[:4]
        iklan_top = Iklan.objects.filter(nomor_iklan=1)
        iklan_bottom = Iklan.objects.filter(nomor_iklan=2)
        iklan_middle = Iklan.objects.filter(nomor_iklan=3)
        iklan_upmiddle = Iklan.objects.filter(nomor_iklan=4)
        iklan_123 = Iklan.objects.filter(nomor_iklan=6)

        # Tampilkan 5 posting per halaman
        paginator = Paginator(queryset, 14)
        page = request.GET.get('page')

        try:
            post_list = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver the first page
            post_list = paginator.page(1)
        except EmptyPage:
            # If page is out of range, deliver last page of results
            post_list = paginator.page(paginator.num_pages)

        # Tambahkan logika pencarian jika parameter 'q' ditemukan dalam request.GET
        q = request.GET.get('q')
        if q:
            search_results = Post.objects.filter(
                Q(title__icontains=q) | Q(slug__icontains=q),
                status=1
            )
            return render(request, "blog/index.html", {
                'data': search_results,
                'post_list': post_list,
                'randompost': randompost,
                'kategori': kategori,
                'headline_list': headline_list,
                'iklan_top': iklan_top,
                'iklan_bottom': iklan_bottom,
                'iklan_middle': iklan_middle,
                'iklan_upmiddle': iklan_upmiddle,
                'iklan_123': iklan_123,
            })

        data = {
                'data': queryset,
                'post_list': post_list,
                'randompost': randompost,
                'popular_posts': popular_posts,
                'kategori': kategori,
                'headline_list': headline_list,
                'iklan_top': iklan_top,
                'iklan_bottom': iklan_bottom,
                'iklan_middle': iklan_middle,
                'iklan_upmiddle': iklan_upmiddle,
                'iklan_123': iklan_123,   
    }

        return render(request, self.template_name, data)

def docs(request):
    # response = redirect('/')
    # return response
    return render(request,"blog/lozad.html") 

def pindah(request, id, slug):
    # Gunakan get_object_or_404 untuk mengambil objek Post berdasarkan ID
    post = get_object_or_404(Post, id=id, status=1)

    # Sekarang Anda memiliki objek 'post' yang sesuai dengan ID yang diberikan
    # Anda dapat melakukan apa pun yang Anda inginkan dengan objek ini, misalnya, mengirimkannya ke template
    return render(request, "blog/detailpost.html", {'post': post})

def cari(request):
    q = request.GET.get('q')

    print(q)
    return HttpResponse("asdasd")

@csp_exempt
def search(request):
    q = request.GET.get('q')

    if q:
        results = Post.objects.filter(Q(title__icontains=q) | Q(slug__icontains=q), status=1)[:30]

        if request.headers.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            # If it's an AJAX request, return JSON response
            data = [{'title': post.title, 'url': post.get_absolute_url()} for post in results]
            return JsonResponse({'results': data})
        else:
            # If it's not an AJAX request, render the search results page
            return render(request, 'blog/hasilcari.html', {'results': results})
    else:
        # If there's no query parameter 'q', you may want to handle this case accordingly.
        # For now, let's redirect to the home page.
        return redirect('home')
    
@csp_exempt
def PostList(request):
    kategori = Kategori.objects.all()
    now = timezone.now()
    queryset = Post.objects.filter(Q(status=1, publish_date__lte=now) | Q(status=2, publish_date__lte=now)).order_by('-created_on').select_related('kategori')
    randompost = random.sample(list(queryset), min(len(queryset), 3))
    popular_posts = Post.objects.filter(status=1).order_by('-views')[:6]
    hukum_posts = Post.objects.filter(status=1, kategori__slug='hukum').order_by('-publish_date')[:6]
    politik_posts = Post.objects.filter(status=1, kategori__slug='politik').order_by('-publish_date')[:6]
    news_posts = Post.objects.filter(status=1, kategori__slug='news').order_by('-publish_date')[:6]

    # Menambahkan definisi latest_headline
    headline_list = Post.objects.filter(is_headline=True, status=1)[:4]
    iklan_top = Iklan.objects.filter(nomor_iklan=1)
    iklan_bottom = Iklan.objects.filter(nomor_iklan=2)
    iklan_middle = Iklan.objects.filter(nomor_iklan=3)
    iklan_upmiddle = Iklan.objects.filter(nomor_iklan=4)
    iklan_123 = Iklan.objects.filter(nomor_iklan=6)
    iklanlebar = Iklan.objects.filter(nomor_iklan=7)

     # Tampilkan 5 posting per halaman
    paginator = Paginator(queryset, 20)
    page = request.GET.get('page')

    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page
        post_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver last page of results
        post_list = paginator.page(paginator.num_pages)

    # Tambahkan logika pencarian jika parameter 'q' ditemukan dalam request.GET
    q = request.GET.get('q')
    if q:
        search_results = Post.objects.filter(
            Q(title__icontains=q) | Q(slug__icontains=q),
            status=1
        )
        return render(request, "blog/index.html", {
            'data': search_results,
            'post_list': post_list,
            'randompost': randompost,
            'kategori': kategori,
            'headline_list': headline_list,
            'iklan_top': iklan_top,
            'iklan_bottom': iklan_bottom,
            'iklan_middle': iklan_middle,
            'iklan_upmiddle': iklan_upmiddle,
            'iklan_123': iklan_123,
            'iklanlebar': iklanlebar,
        })

    data = {
        'data': queryset,
        'post_list': post_list,
        'randompost': randompost,
        'popular_posts': popular_posts,
        'hukum_posts': hukum_posts,
        'politik_posts': politik_posts,
        'news_posts' : news_posts,
        'kategori': kategori,
        'headline_list': headline_list,
        'iklan_top': iklan_top,
        'iklan_bottom': iklan_bottom,
        'iklan_middle': iklan_middle,
        'iklan_upmiddle': iklan_upmiddle,
        'iklan_123': iklan_123,
        'iklanlebar': iklanlebar,

        
    }

    return render(request, "blog/index.html", data)

@csp_exempt
def PostDetail(request, slug):
    dt = Post.objects.filter(status=1).select_related('kategori', 'author').get(slug=slug)
    dt.views += 1  # Increment the view count
    dt.save()
    # print(dt.slug)
    kategori = Kategori.objects.all()
    queryset = Post.objects.all().filter(status=1)
    randompost = random.sample(list(queryset), min(len(queryset),6))
    popular_posts = Post.objects.filter(status=1).order_by('-views')[:6]

    iklan_top = Iklan.objects.filter(nomor_iklan=1)
    iklan_bottom = Iklan.objects.filter(nomor_iklan=2)
    iklan_middle = Iklan.objects.filter(nomor_iklan=3)
    iklan_upmiddle = Iklan.objects.filter(nomor_iklan=4)
    iklan_123 = Iklan.objects.filter(nomor_iklan=6)
    
    
    data = {
        'post': dt,
        'randompost': randompost,
        'popular_posts': popular_posts,
        'kategori': kategori,
        'iklan_top': iklan_top,
        'iklan_bottom': iklan_bottom,
        'iklan_middle': iklan_middle,
        'iklan_upmiddle': iklan_upmiddle,
        'iklan_123': iklan_123,
    }
    return render(request,"blog/detailpost.html",data)

@csp_exempt
def tagged(request, slug):
    kategori = Kategori.objects.all()
    tag = get_object_or_404(Tag, slug=slug)
    # Filter posts by tag name  
    posts = Post.objects.filter(tags=tag,status=1)
    queryset = Post.objects.all().filter(status=1)
    randompost = random.sample(list(queryset), min(len(queryset),4))
    
    paginator = Paginator(posts, 5)  # 3 posts in each page
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
    return render(request, 'blog/tag.html', context)

@csp_exempt
def KategoriShow(request, slug):
    # Menggunakan get_object_or_404 untuk mendapatkan objek Kategori berdasarkan slug
    kategori = get_object_or_404(Kategori, slug=slug)
    
    # Menggunakan related_name 'blog_kategori' untuk mendapatkan posting yang terkait dengan kategori
    dt = Post.objects.filter(status=1, kategori=kategori)
    
    namakategori = kategori.kategori

    queryset = Post.objects.filter(status=1)
    randompost = random.sample(list(queryset), min(len(queryset), 3))

    paginator = Paginator(dt, 5)  # 5 posts per page
    page = request.GET.get('page')

    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page
        post_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver last page of results
        post_list = paginator.page(paginator.num_pages)

    data = {
        'namakategori': namakategori,
        'hitung': dt.count(),
        'slug': slug,
        'post_list': post_list,
        'randompost': randompost,
        'kategori': kategori,
        'page': page,
    }

    return render(request, "blog/kategori.html", data)

@csp_exempt
def hand404(request,exception):
    queryset = Post.objects.all().filter(status=1)
    kategori = Kategori.objects.all()
    randompost = random.sample(list(queryset), min(len(queryset),4))
    data = {
        'randompost':randompost,
        'kategori':kategori,
    }
    return render(request,"blog/404.html",data)
    
@csp_exempt    
def hand500(request):
    return render(request, 'blog/500.html', status=500)
#     # return HttpResponse(dt)
    
# API
@api_view(['GET', ])
def APIPostList(request):
    kategori = Kategori.objects.all()
    queryset = Post.objects.filter(status=1).all()
    randompost = random.sample(list(queryset), min(len(queryset),4))
    data = []
    nextPage = 1
    previousPage = 1
    paginator = Paginator(queryset, 5)  # 3 posts in each page
    page = request.GET.get('page', 1)
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
    
    serializer = ArticleSerializer(data,context={'request': request},many=True)
    kat = KategoriSerializer(kategori ,many=True)    
    randompostt = ArticleSerializer(randompost,many=True)
    
    if data.has_next():
        nextPage = data.next_page_number()
    if data.has_previous():
        previousPage = data.previous_page_number()
    
    data = {
        'data':serializer.data,
        'kategori': kat.data,
        'randompost': randompostt.data,
        'halaman': "cobaa",
        'count': paginator.count, 
        'numpages' : paginator.num_pages, 
        'nextlink': '/api/?page=' + str(nextPage), 
        'prevlink': '/api/?page=' + str(previousPage)

    }

    return Response(data)
    # return render(request,"blog/index.html",data) 

def APIPostDetail(request, slug):
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
    return render(request,"blog/detailpost.html",data)


def load_more_posts(request):
    # Convert 'page' parameter to an integer
    page = int(request.GET.get('page', 1))

    posts_per_load = 5
    start_index = (page - 1) * posts_per_load
    end_index = start_index + posts_per_load

    posts = Post.objects.filter(status=1).order_by('-created_on').select_related('kategori')[start_index:end_index]

    data = {
        'posts': [{'title': post.title, 'slug': post.slug} for post in posts],
    }

    # Use a JsonResponse to send the new posts back to the client
    return JsonResponse(data)