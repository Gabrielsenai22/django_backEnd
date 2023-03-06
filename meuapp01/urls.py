from django.urls import path
from . import views

urlpatterns = [
   #path('cadastro/', views.cadastro, name='cadastro'),
   #path('login/', views.login, name='login'),
   path('/', views.raiz, name='raiz'),
   path('produtos/', views.produtos, name='produtos'),
   path("cadastrar/", views.consultar_ultimo, name="consulta")
]
