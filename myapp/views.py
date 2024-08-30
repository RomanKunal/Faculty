from django.shortcuts import render

from .models import Faculty

def home(request):
    faculties=Faculty.objects.all()
    return render(request,'home.html',{'faculties':faculties})

def fetch(request):
    courses = Faculty.objects.filter(Subject__icontains='django')  
    return render(request, 'Fetch.html', {'courses': courses})