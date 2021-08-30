
from django.db.models import Sum
from django.shortcuts import render, get_object_or_404, redirect
from django.core.files.storage import FileSystemStorage
import json
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotFound
from django.http import Http404
from django.core.paginator import Paginator
import datetime
from .models import *
from .forms import *

@login_required
def home(request):
    home = Home.objects.all()
    return render(request, 'front/home.html', {'home': home})

def homeView(request, id):
    home = get_object_or_404(Home, pk=id)
    return render(request, 'front/homez.html', {'home': home})

@login_required
def dados(request):
    return render(request, 'front/dados.html')

@login_required
def pesquisas(request):
    return render(request, 'front/pesquisas.html')

@login_required
def tutoriaispalestras(request):
    return render(request, 'front/tutoriaispalestras.html')

@login_required
def boletins(request):
    return render(request, 'front/boletins.html')