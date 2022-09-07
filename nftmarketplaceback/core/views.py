from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from django.shortcuts import render
from .serializers import *
from .models import *
from .forms import *
from rest_framework import status


class LatestListNft(APIView):

    def get(self, request, format=None):

        items = Item.objects.all()[0:4]
        serializer = GetAllItems(items, many=True)
        return Response(serializer.data)

    
class GetSpecifiedItem(APIView):
    
    def get_object(self, item_slug):

        try:
            return Item.objects.get(slug=item_slug)
        except Item.DoesNotExist:
            raise Http404

    def get(self, request, item_slug, format=True):

        item = self.get_object(item_slug)
        serializer = GetAllItems(item)
        return Response(serializer.data)

class CreateItem(APIView):

    def post(self, request, foramt=None):

        serializer = GetAllItems(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreatItemPart2(APIView):

    serializer = GetAllItems()

    def get_queryset(self):

        items = Item.objects.all()
        return items

    def get(self, request, *args, **kwargs):
        
        items = self.get_queryset()
        serializer = GetAllItems(items, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):

        item_data = request.data

        new_item = Item.objects.create(title=item_data['title'], price=item_data['price'], description=item_data['description'], creator=item_data['creator'])
        new_item.save()

        serializer = GetAllItems(data=request.data)
        return Response(serializer.data)
