from django.urls import path
from . import views

urlpatterns = [
    # Autores (vistas normales)
    path('autores/', views.lista_autores, name='lista_autores'),
    path('autores/crear/', views.crear_autor, name='crear_autor'),
    path('autores/editar/<int:pk>/', views.editar_autor, name='editar_autor'),
    path('autores/eliminar/<int:pk>/', views.eliminar_autor, name='eliminar_autor'),

    # Libros (vistas normales + genericas ya existentes)
    path('libros/', views.lista_libros, name='lista_libros'),
    path('libros/crear/', views.CrearLibroView.as_view(), name='crear_libro'),
    path('libros/editar/<int:pk>/', views.EditarLibroView.as_view(), name='editar_libro'),

    # Autores (vistas genericas)
    path('generico/autores/', views.ListaAutorGenericaView.as_view(), name='lista_autores_generica'),
    path('generico/autores/crear/', views.CrearAutorGenericaView.as_view(), name='crear_autor_generica'),
    path('generico/autores/editar/<int:pk>/', views.EditarAutorGenericaView.as_view(), name='editar_autor_generica'),
    path('generico/autores/eliminar/<int:pk>/', views.EliminarAutorGenericaView.as_view(), name='eliminar_autor_generica'),

    # Libros (vistas genericas)
    path('generico/libros/', views.ListaLibroGenericaView.as_view(), name='lista_libros_generica'),
    path('generico/libros/crear/', views.CrearLibroGenericaView.as_view(), name='crear_libro_generica'),
    path('generico/libros/editar/<int:pk>/', views.EditarLibroGenericaView.as_view(), name='editar_libro_generica'),
    path('generico/libros/eliminar/<int:pk>/', views.EliminarLibroGenericaView.as_view(), name='eliminar_libro_generica'),
]
