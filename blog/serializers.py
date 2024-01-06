from rest_framework import serializers
from .models import Post, Kategori
from django.contrib.auth.models import User
from rest_framework.fields import CurrentUserDefault
from django.contrib.auth import get_user_model

# User = get_user_model()

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
        ]
class KategoriSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kategori
        fields = ('kategori', 'slug')
        depth = 1

class ArticleSerializer(serializers.ModelSerializer):
    kategori = serializers.CharField(source="kategori.kategori")
    # kategori = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    # banner = serializers.SomeCustomImageField
    # kategori = KategoriSerializer(many=True,read_only=True)
    author =  serializers.CharField(source="author.username")
    class Meta:
        model = Post
        # read_only_fields = ('id', 'kategori_kategori')
        # fields = "__all__"
        fields = "__all__"
        depth = 3