# Generated by Django 4.0.5 on 2022-06-29 15:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Creator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=50, unique=True)),
                ('bio', tinymce.models.HTMLField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, max_length=400, unique=True)),
                ('profile_pic', django_resized.forms.ResizedImageField(blank=True, crop=None, default=None, force_format=None, keep_meta=True, null=True, quality=100, scale=None, size=[50, 80], upload_to='authors')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('slug', models.SlugField(unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.creator')),
            ],
            options={
                'verbose_name': 'NFT',
                'ordering': ('-date_added',),
            },
        ),
    ]
