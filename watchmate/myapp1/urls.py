from django.urls import path
from myapp1.views import movie_list

urlpatterns = [
    path('list/'. movie_list, name='movie-list'),
]