from django.db import models

class Home(models.Model):

    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.title

class Consumo(models.Model):

    Tipo = models.CharField(max_length=10000)
    Classe = models.CharField(max_length=10000)
    Valor = models.CharField(max_length=10000)

class Consumidores(models.Model):

    Bairros = models.CharField(max_length=10000)
    Mín = models.CharField(max_length=10000)
    Max = models.CharField(max_length=10000)
    Média = models.CharField(max_length=10000)
    Moradores = models.CharField(max_length=10000)
    Hab_Total = models.CharField(max_length=10000)
    Renda_Média_por_Morador = models.CharField(max_length=10000)
    Renda_Média_Familiar = models.CharField(max_length=10000)

class Empresas(models.Model):

    Razão_Social = models.CharField(max_length=10000)
    CNPJ = models.CharField(max_length=10000)
    Atividade_Econômica_CNAE = models.CharField(max_length=10000)
    Porte = models.CharField(max_length=10000)
    Endereço = models.CharField(max_length=10000)

class Pesquisa(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title