from django.urls import path

from .views import *

urlpatterns = [
    path('register/', register_form, name='register')
]