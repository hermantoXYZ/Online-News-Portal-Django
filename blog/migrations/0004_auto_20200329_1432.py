# Generated by Django 3.0.4 on 2020-03-29 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_banner'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='meta_deskripsi',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='meta_keyword',
            field=models.CharField(max_length=200, null=True),
        ),
    ]