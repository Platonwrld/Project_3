from rest_framework import serializers
from .models import *


class GetAllItems(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = [
            'title',
            'price',
            'get_image',
            'get_absolute_url',
            'description',
            'creator',

        ]

