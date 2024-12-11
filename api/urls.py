from django.urls import path
from .views import *

urlpatterns = [
    path('', get_items),
    path('add/', add_item),
]