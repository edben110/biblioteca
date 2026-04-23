from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Autor, Libro
from .forms import AutorForm, LibroForm

# =============================================
# CRUD Autores
# =============================================

def lista_autores(request):
    autores = Autor.objects.all()
    return render(request, 'gestion/lista_autores.html', {'autores': autores})

def crear_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_autores')
    else:
        form = AutorForm()
    return render(request, 'gestion/crear_autor.html', {'form': form})

def editar_autor(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
        form = AutorForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
            return redirect('lista_autores')
    else:
        form = AutorForm(instance=autor)
    return render(request, 'gestion/editar_autor.html', {'form': form})

def eliminar_autor(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
        autor.delete()
        return redirect('lista_autores')
    return render(request, 'gestion/autor_confirm_delete.html', {'autor': autor})
# =============================================
# CRUD Libros
# =============================================

# Vista normal (función) - Listar libros
def lista_libros(request):
    libros = Libro.objects.select_related('autor').all()
    return render(request, 'list_view.html', {'libros': libros})

# Vista genérica (clase) - Crear libro
class CrearLibroView(CreateView):
    model = Libro
    form_class = LibroForm
    template_name = 'create_view.html'
    success_url = reverse_lazy('lista_libros')

# Vista genérica (clase) - Editar libro
class EditarLibroView(UpdateView):
    model = Libro
    form_class = LibroForm
    template_name = 'edit_view.html'
    success_url = reverse_lazy('lista_libros')


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
