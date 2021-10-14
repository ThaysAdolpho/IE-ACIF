from django.db import models


class Home(models.Model):

    title = models.CharField(max_length=255)
    previa = models.CharField(max_length=1000, default='Some String')
    description = models.TextField(max_length=10000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.title

class Consumo(models.Model):

    TIPO = models.CharField(max_length=10000)
    CLASSE = models.CharField(max_length=10000)
    VALOR = models.CharField(max_length=10000)

class Consumidores(models.Model):

    Bairros = models.CharField(max_length=10000)
    Min = models.CharField(max_length=10000)
    Max = models.CharField(max_length=10000)
    Media = models.CharField(max_length=10000)
    Moradores = models.CharField(max_length=10000)
    HabitantesTotal = models.CharField(max_length=10000)
    RendaMediapormorador = models.CharField(max_length=10000)
    RendaMediaFamiliar = models.CharField(max_length=10000)

class Empresas(models.Model):

    Razao = models.CharField(max_length=10000)
    CNPJ = models.CharField(max_length=10000)
    ATIVIDADE = models.CharField(max_length=10000)
    PORTE = models.CharField(max_length=10000)
    Endereco = models.CharField(max_length=10000)

class Pesquisa(models.Model):
    title = models.CharField(max_length=255)
    previa = models.CharField(max_length=1000, default='Some String')
    description = models.TextField(max_length=10000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class TutoriaisPalestras(models.Model):

    STATUS = (
        ('Tutoriais', 'Tutoriais'),
        ('Palestras', 'Palestras'),
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=9, choices= STATUS)
    

    def __str__(self):
        return self.title