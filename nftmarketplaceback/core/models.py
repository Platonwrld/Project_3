from tokenize import blank_re
from django.db import models
from django.utils.text import slugify
from django.core.files import File
from PIL import Image
from io import BytesIO
from django.urls import reverse
from django.contrib.auth.models import User
from django_resized import ResizedImageField
from tinymce.models import HTMLField


class Creator(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=50, unique=True)
    bio = HTMLField(blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, max_length=400)
    profile_pic = ResizedImageField(size=[50, 80], quality=100, upload_to='authors', default=None, null=True, blank=True)

    def __str__(self):
        return self.nickname

    def save(self, *args, **kwargs):
        """ Метод для сохранения title как slug, если нету slug """
        if not self.slug:
            self.slug = slugify(self.nickname)
        super(Creator, self).save(*args, **kwargs)


class Item(models.Model):

    creator = models.ForeignKey(Creator, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=50)
    description = models.TextField()
    slug = models.SlugField(max_length=50, unique=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_added',)
        verbose_name = 'NFT'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/{self.slug}/'

    # def get_absolute_url(self):
    #     return reverse('item', kwargs={'item_slug': self.slug})

    # save slug 
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Item, self).save(*args, **kwargs)

    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''
    

    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return 'http://127.0.0.1:8000' + self.thumbnail.url
            else:
                return ''
    
    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.title)

        return thumbnail