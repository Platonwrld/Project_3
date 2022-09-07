from django.forms import ModelForm
from .models import *


class CreateItem(ModelForm):

    class Meta:
        model = Item
        fields = ['title', 'description', 'price', 'image']