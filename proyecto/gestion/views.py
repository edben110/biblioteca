from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from .models import Autor, Libro
from .forms import AutorForm, LibroForm


class HomeView(TemplateView):
    template_name = 'home.html'

# =============================================
# CRUD Generico (Class-Based Views)
# =============================================

# Autor - vistas genericas
class ListaAutorGenericaView(ListView):
    model = Autor
    template_name = 'genericas/autores/lista_autor_generica.html'
    context_object_name = 'autores'


class CrearAutorGenericaView(CreateView):
    model = Autor
    form_class = AutorForm
    template_name = 'genericas/autores/crear_autor_generica.html'
    success_url = reverse_lazy('lista_autores_generica')


class EditarAutorGenericaView(UpdateView):
    model = Autor
    form_class = AutorForm
    template_name = 'genericas/autores/editar_autor_generica.html'
    success_url = reverse_lazy('lista_autores_generica')


class EliminarAutorGenericaView(DeleteView):
    model = Autor
    template_name = 'genericas/autores/eliminar_autor_generica.html'
    success_url = reverse_lazy('lista_autores_generica')
    context_object_name = 'autor'


# Libro - vistas genericas
class ListaLibroGenericaView(ListView):
    model = Libro
    template_name = 'genericas/libros/lista_libro_generica.html'
    context_object_name = 'libros'

    def get_queryset(self):
        return Libro.objects.select_related('autor').all()


class CrearLibroGenericaView(CreateView):
    model = Libro
    form_class = LibroForm
    template_name = 'genericas/libros/crear_libro_generica.html'
    success_url = reverse_lazy('lista_libros_generica')


class EditarLibroGenericaView(UpdateView):
    model = Libro
    form_class = LibroForm
    template_name = 'genericas/libros/editar_libro_generica.html'
    success_url = reverse_lazy('lista_libros_generica')


class EliminarLibroGenericaView(DeleteView):
    model = Libro
    template_name = 'genericas/libros/eliminar_libro_generica.html'
    success_url = reverse_lazy('lista_libros_generica')
    context_object_name = 'libro'
