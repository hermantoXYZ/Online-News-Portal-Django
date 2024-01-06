from . import views
from .views import ListViewSet
from django.urls import path
from .feeds import LatestPostsFeed, KategoriFeed
from django.shortcuts import redirect
from rest_framework import routers
from django.conf.urls import include
from .views import StaticPageView, IndexView

urlpatterns = [
    path('', views.PostList, name='home'),
    path('api/', views.APIPostList, name='homeAPI'),
    path('api2/',views.ListViewSet.as_view()),
    path('404/', views.hand404, name='404'),
    path('500/', views.hand500, name='500'),
    path('cari/', views.cari, name='cari'),
    path('docs-pribadi/', views.docs, name='docs'),
    path('read/<int:id>/<slug:slug>/', views.pindah, name='pindah'),
    path('search/', views.search, name='search'),
    path("rss/feed/", LatestPostsFeed(), name="post_feed"),
    path("rss/kategori/", KategoriFeed(), name="kategori_feed"),
    path('tag/<slug:slug>/', views.tagged, name="tagged"),    
    path('kategori/<slug:slug>/', views.KategoriShow, name='kategori_show'),
    path('read/<slug:slug>/', views.PostDetail, name='post_detail'),
    path('read/<int:pk>/', views.PostDetail, name='post_detail_by_id'),
    path('page/<slug:slug>/', StaticPageView.as_view(), name='static_page'),
    path('indeks/', IndexView.as_view(), name='index'),


]

