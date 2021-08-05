from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name= 'home'),
    path('dados/', views.dados, name='dados'),
    path('pesquisas/', views.pesquisas, name='pesquisas'),
    path('boletins/', views.boletins, name= 'boletins'),
    path('tutoriaispalestras/', views.tutoriaispalestras, name= 'tutoriaispalestras'),
]