from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Hello, World!")

def about(request):
    return HttpResponse("This is my Django application!")