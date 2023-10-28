from django.shortcuts import render
from .models import *
# Create your views here.


def start_page(request):
    data = Genre.objects.all()
    context = {
        "data": data
    }
    return render(request, 'app/index.html', context=context)


def category_page(request, parameter):
    data = Singer.objects.filter(genre=Genre.objects.get(title=parameter))
    context = {
        "data": data
    }
    return render(request, 'app/genre.html', context=context)


def singer_page(request, parameter, singer):
    data = Singer.objects.get(name=singer)
    context = {
        "singer": data
    }
    return render(request, 'app/singer.html', context=context)

