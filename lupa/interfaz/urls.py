from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.nosotros, name='nosotros'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('prueba/', views.prueba, name='prueba'),
    path('pagina_prueba/', views.pagina_prueba, name='pagina_prueba'),
    path('cartas/crear_carta/', views.crear_carta, name='crear_carta'),
    path('cartas/modificar_carta/<id>/', views.modificar_carta, name='modificar_carta'),
    path('cartas/eliminar_carta/<id>/', views.eliminar_carta, name='eliminar_carta'),
]