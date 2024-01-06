from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import GenericSitemap
from blog.sitemaps import PostSitemap, Halamansitemap
from blog.models import Kategori, Post
from django.views.static import serve
from blog import views
from django.views.generic.base import TemplateView
from taggit.models import Tag
from django.template.response import TemplateResponse
from django.views import View

admin.site.site_header = "Panel | Sudut Kota"
admin.site.site_title = "AdminPortal | Sudut Kota"
admin.site.index_title = "Selamat datang di Website Sudut Kota"

sitemaps = {
    "page": Halamansitemap,
    "kategori": GenericSitemap(
        {"queryset": Kategori.objects.all(), "changefreq": "daily"},
        priority=0.9,
    ),
    "posts": PostSitemap,
}

class OneSignalSDKView(View):
    def get(self, request, *args, **kwargs):
        return TemplateResponse(
            request=request,
            template="notif/{}".format(kwargs["path"].split("?")[0]),
            content_type="application/javascript",
        )

class PWA(View):
    def get(self, request, *args, **kwargs):
        return TemplateResponse(
            request=request,
            template="pwa/{}".format(kwargs["path"].split("?")[0]),
            content_type="application/javascript",
        )

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("blog.urls")),
    path("amp/", include("amp.urls")),
    # path('404/', views.handler404, name='404'),
    # path('500/', views.handler500, name='500'),
    re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
    re_path(
        r"^amp/media/(?P<path>.*)$",
        serve,
        {"document_root": settings.MEDIA_ROOT},
    ),
    re_path(
        r"^static/(?P<path>.*)$", serve, {"document_root": settings.STATIC_DIR}
    ),
    re_path(
        r"^amp/static/(?P<path>.*)$", serve, {"document_root": settings.STATIC_DIR}
    ),
    path("ckeditor/", include("ckeditor_uploader.urls")),
    path("sitemap.xml/", sitemap, {"sitemaps": sitemaps}, name="sitemap"),
    path(
        "robots.txt",
        TemplateView.as_view(template_name="blog/robots.txt", content_type="text/plain"),
    ),
    re_path(r"^(?P<path>OneSignalSDK.*)$", OneSignalSDKView.as_view()),
    re_path(r"^(?P<path>pwabuilder.*)$", PWA.as_view()),
    re_path(r"^amp/(?P<path>OneSignalSDK.*)$", OneSignalSDKView.as_view()),
    re_path(r"^amp/(?P<path>pwabuilder.*)$", PWA.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_DIR)

handler404 = views.hand404
handler500 = views.hand500
