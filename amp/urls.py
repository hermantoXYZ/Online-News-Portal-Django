from amp import views
from django.urls import path
from django.shortcuts import redirect
# app_name = 'amp'
# handler500 = views.handler500

urlpatterns = [
    path('', views.PostList, name='amp_home'),
    path('tag/<slug:slug>/amp', views.tagged, name="tagged_amp"),    
    path('kategori/<slug:slug>/amp', views.KategoriShow, name='kategori_show_amp'),
    path('read/<slug:slug>/amp', views.PostDetail, name='amp_post_detail'),
]

# handler404 = views.handler404