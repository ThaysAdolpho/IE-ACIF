from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers


class HomeViewset(viewsets.ModelViewSet):
    queryset = models.Home.objects.all()
    serializer_class = serializers.HomeSerializer


class ConsumoViewset(viewsets.ModelViewSet):
    queryset = models.Consumo.objects.all()
    serializer_class = serializers.ConsumoSerializer


class ConsumidoresViewset(viewsets.ModelViewSet):
    queryset = models.Consumidores.objects.all()
    serializer_class = serializers.ConsumidoresSerializer


class EmpresasViewset(viewsets.ModelViewSet):
    queryset = models.Empresas.objects.all()
    serializer_class = serializers.EmpresasSerializer


class PesquisaViewset(viewsets.ModelViewSet):
    queryset = models.Pesquisa.objects.all()
    serializer_class = serializers.PesquisaSerializer


class TutoriaisPalestrasViewset(viewsets.ModelViewSet):
    queryset = models.TutoriaisPalestras.objects.all()
    serializer_class = serializers.TutoriaisPalestrasSerializer