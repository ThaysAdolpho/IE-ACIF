from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name= 'home'),
    path('dados/', views.dados, name='dados'),
    path('pesquisas/', views.pesquisas, name='pesquisas'),
    path('boletins/', views.boletins, name= 'boletins'),
    path('tutoriaispalestras/', views.tutoriaispalestras, name= 'tutoriaispalestras'),
    path('pesquisa/<int:id>', views.pesquisaView, name='pesquisaView'),
    path('home/<int:id>', views.homeView, name='homeView'),
    path('bairro/', views.bairro, name='bairro'),
    path('consumo/', views.consumo, name='consumo'),
    path('empresa/', views.empresa, name='empresa'),
    # path('tutoriaispalestras/<int:id>', views.tutoriaispalestrasView, name= 'tutoriaispalestrasView'),
]