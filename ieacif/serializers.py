from rest_framework import serializers, status
from ieacif.models import *


class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = '__all__'


class ConsumoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consumo
        fields = '__all__'


class ConsumidoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consumidores
        fields = '__all__'


class EmpresasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresas
        fields = '__all__'


class PesquisaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pesquisa
        fields = '__all__'


class TutoriaisPalestrasSerializer(serializers.ModelSerializer):
    class Meta:
        model = TutoriaisPalestras
        fields = '__all__'