from django.urls import path
from .views.views import *

urlpatterns = [
    path('', get_users),
    path('add/', add_user),
    path('users/<str: name>', get_by_name),

]