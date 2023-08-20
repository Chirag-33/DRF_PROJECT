from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from myapp1.models import Movie
# Create your views here.

def movie_list(request):
    movies = Movie.objects.all()

    data = {
        'movies':list(movies.values())
    }

    return JsonResponse