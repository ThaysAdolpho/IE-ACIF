
from django.db.models import Sum
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
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
    homes = Home.objects.all()
    return render(request, 'front/home.html', {'homes': homes})

@login_required
def homeView(request, id):
    home = get_object_or_404(Home, pk=id)
    return render(request, 'front/homeview.html', {'home': home})
    

@login_required
def dados(request):
    dado_list = Consumidores.objects.all()
    
    paginator = Paginator(dado_list, 5)

    page = request.GET.get('page')

    dado = paginator.get_page(page)

    return render(request, 'front/dados.html', {'dado': dado})

@login_required
def bairro(request):
    bairro_list = Consumidores.objects.all()
    
    paginator = Paginator(bairro_list, 8)

    page = request.GET.get('page')

    bairro = paginator.get_page(page)

    return render(request, 'front/bairro.html', {'bairro': bairro})


@login_required
def consumo(request):
    consumo_list = Consumo.objects.all()
    
    paginator = Paginator(consumo_list, 6)

    page = request.GET.get('page')

    consumo = paginator.get_page(page)

    return render(request, 'front/consumo.html', {'consumo': consumo})


@login_required
def empresa(request):
    empresa_list = Empresas.objects.all()
    
    paginator = Paginator(empresa_list, 5)

    page = request.GET.get('page')

    empresa = paginator.get_page(page)

    return render(request, 'front/empresa.html', {'empresa': empresa})


@login_required
def pesquisas(request):
    pesquisas = Pesquisa.objects.all()
    return render(request, 'front/pesquisas.html', {'pesquisas': pesquisas})

@login_required
def pesquisaView(request, id):
    pesquisa = get_object_or_404(Pesquisa, pk=id)
    return render(request, 'front/pesquisa.html', {'pesquisa': pesquisa})

@login_required
def tutoriaispalestras(request):
    tps = TutoriaisPalestras.objects.all()
    return render(request, 'front/tutoriaispalestras.html', {'tps': tps})

# @login_required
# def tutoriaispalestrasView(request, id):
#     tutoriaispalestras = get_object_or_404(TutoriaisPalestras, pk=id)
#     return render(request, 'front/tutoriaispalestrasview.html', {'tutoriaispalestras': tutoriaispalestras})

@login_required
def boletins(request):
    return render(request, 'front/boletins.html')