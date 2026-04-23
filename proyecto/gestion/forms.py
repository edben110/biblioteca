from django import forms
from .models import Autor, Libro


class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'correo', 'nacionalidad', 'fecha_nacimiento', 'biografia']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre completo'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'correo@ejemplo.com'}),
            'nacionalidad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Colombiana'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'biografia': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Breve biografía (opcional)'}),
        }

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        if len(nombre) < 3:
            raise forms.ValidationError('El nombre debe tener al menos 3 caracteres.')
        return nombre


class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'fecha_publicacion', 'genero', 'isbn', 'autor']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título del libro'}),
            'fecha_publicacion': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'genero': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Ficción, Historia'}),
            'isbn': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 978-3-16-148410-0'}),
            'autor': forms.Select(attrs={'class': 'form-select'}),
        }

    def clean_isbn(self):
        isbn = self.cleaned_data['isbn']
        limpio = isbn.replace('-', '').replace(' ', '')
        if not limpio.isdigit() or len(limpio) not in (10, 13):
            raise forms.ValidationError('El ISBN debe tener 10 o 13 dígitos.')
        return isbn
