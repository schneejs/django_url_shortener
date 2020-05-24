from django.urls import path, include
from main.views import *

urlpatterns = [
    path('shorten/', Shorten.as_view()),
    path('<str:alias>/', Alias.as_view()),
]
