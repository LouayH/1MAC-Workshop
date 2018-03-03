from django.http import HttpResponse
from django.shortcuts import render
from . import tests

def index(request):
    context = {
        'posts': tests.post_store.posts
    }
    return render(request, 'index.html', context)