from django.shortcuts import render

def home(request):
    return render(request, 'app1/home.html')

def sample1(request):
    return render(request, 'app1/sample1.html')


# Create your views here.
