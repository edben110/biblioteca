from django.urls import path
from . import views

urlpatterns = [
    # Autores
    path('autores/', views.lista_autores, name='lista_autores'),
    path('autores/crear/', views.crear_autor, name='crear_autor'),
    path('autores/editar/<int:pk>/', views.editar_autor, name='editar_autor'),

    # Libros
    path('libros/', views.lista_libros, name='lista_libros'),
    path('libros/crear/', views.CrearLibroView.as_view(), name='crear_libro'),
    path('libros/editar/<int:pk>/', views.EditarLibroView.as_view(), name='editar_libro'),
]
