from django.shortcuts import render, HttpResponse
from .models import About

# Create your views here.
def about(request):
    equipo = About.objects.all()
    return render(request, 'about/about.html', {'equipo':equipo})