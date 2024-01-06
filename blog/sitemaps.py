from django.contrib.sitemaps import Sitemap
from .models import Post, Kategori
from django.shortcuts import reverse

class PostSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8

    def items(self):
        return Post.objects.filter(status=1)

    def lastmod(self, obj):
        return obj.updated_on

# class KategoriSitemap(Sitemap):
#     changefreq = "always"
#     priority = 0.8

#     def items(self):
#         return Kategori.objects.all()

#     # def lastmod(self, obj):
#     #     return obj.updated_on

class Halamansitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8

    def items(self):
        return ['home','post_feed','kategori_feed']
    def location(self, item):
        return reverse(item)

    # def location(self, item):
    #     return reverse(item)