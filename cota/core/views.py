from django.shortcuts import render, HttpResponse
from nodos.models import Book
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from django.core.serializers import serialize
from django.core.serializers.json import DjangoJSONEncoder

# Create your views here.
def index(request):
    return render(request, 'core/index.html')
