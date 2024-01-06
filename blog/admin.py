from django.contrib import admin
from .models import Post, Kategori, Iklan, StaticPage

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'publish_date', 'created_on')
    list_filter = ('status', 'publish_date')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

class PostKategori(admin.ModelAdmin):
    list_display = ('kategori', 'slug', 'created_on')
    search_fields = ['kategori']
    prepopulated_fields = {'slug': ('kategori',)}

class IklanAdmin(admin.ModelAdmin):
    list_display = ('judul', 'link', 'gambar')
    search_fields = ('judul', 'link')

class StaticPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug',)
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(StaticPage, StaticPageAdmin)
admin.site.register(Iklan, IklanAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Kategori, PostKategori)
# Register your models here.
