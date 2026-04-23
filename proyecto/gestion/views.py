from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView
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
    return render(request, 'gestion/autor_form.html', {'form': form})

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
