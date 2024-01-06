from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager
from django.utils.text import slugify
from django.utils import timezone
from django.urls import reverse


class Kategori(models.Model):
    kategori = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.kategori

    def save(self, *args, **kwargs):
        # Mengisi slug menggunakan fungsi slugify
        self.slug = slugify(self.kategori)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        # Menggunakan slug untuk mendapatkan URL
        return reverse('kategori_show', args=[str(self.slug)])

class PostSearchManager(models.Manager):
    def search(self, query):
        results = self.filter(
            models.Q(title__icontains=query) |
            models.Q(slug__icontains=query) |
            models.Q(content__icontains=query),
            status=1
        )
        return results.values('title', 'get_absolute_url')

class Post(models.Model):
    STATUS_CHOICES = [
        (0, 'Draft'),
        (1, 'Published'),
    ]

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    is_headline = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = RichTextUploadingField(blank=True, null=True)
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE, related_name='blog_kategori')
    tags = TaggableManager(blank=True)
    banner = models.ImageField(upload_to='banner_pics')
    meta_deskripsi = models.TextField(null=True, verbose_name='Caption Picture', blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    publish_date = models.DateTimeField(default=timezone.now, null=True, blank=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)

    # New field for tracking views
    views = models.PositiveIntegerField(default=0)
    meta_keyword = models.CharField(max_length=200, unique=False, null=True, blank=True)

    # Tambahkan manager khusus untuk pencarian
    objects = models.Manager()
    search_manager = PostSearchManager()

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("post_detail", kwargs={"slug": str(self.slug)})

    @property
    def absolute_url(self):
        return self.get_absolute_url()

    def get_search_result_data(self):
        return {'title': self.title, 'absolute_url': self.absolute_url}
  

class Iklan(models.Model):
    judul = models.CharField(max_length=200)
    gambar = models.ImageField(upload_to='iklan_pics')
    link = models.URLField()
    nomor_iklan = models.IntegerField(default=1)

    def __str__(self):
        return self.judul

class StaticPage(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    content = RichTextUploadingField(blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('static_page', args=[str(self.slug)])