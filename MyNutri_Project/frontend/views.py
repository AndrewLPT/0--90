from django.shortcuts import render
# frontend/views.py

def home(request):
    return render(request, 'frontend/home.html')

def dashboard(request):
    return render(request, 'frontend/dashboard.html')

def about(request):
    return render(request, 'frontend/about.html')

