from django.urls import path
from .views import *


urlpatterns = [
    path('items-list/', LatestListNft.as_view(), name='items'),
    path('item/<slug:item_slug>/', GetSpecifiedItem.as_view(), name='item'),
    path('create-item/', CreateItem.as_view(), name='create_item'),
    path('create-item-2/', CreatItemPart2.as_view(), name='create-item-2')
]
