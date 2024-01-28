from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),      #home
    path('sobre/', views.sobre),  #página sobre
    path('contato/', views.contato),  #página contato
    path('recipes/<id>/', views.recipe)  #página contato
]
