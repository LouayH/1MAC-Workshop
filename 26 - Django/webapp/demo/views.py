from django.http import HttpResponse

def index(request):
    return HttpResponse("Hi there, this is my index")

def say_hello(request, name):
    return HttpResponse(f"Hello {name}")