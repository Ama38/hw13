from django.urls import path
from .views import *


urlpatterns = [
    path('', start_page, name='start_page'),
    path('genre/<str:parameter>', category_page, name='genre_page'),
    path('genre/<str:parameter>/singer/<str:singer>', singer_page, name='singer_page')
]
