from django import forms
from django.forms import ModelForm
from .models import Task2

class CrearNuevaTarea(forms.Form):
    title = forms.CharField(label="titulo de tarea", max_length=200)
    description = forms.CharField(label="descripcion de la tarea", widget=forms.Textarea)


class CrearProyecto(forms.Form):
    name = forms.CharField(max_length=200)

class CrearPersona(forms.Form):
    name = forms.CharField(max_length=200)
    age = forms.CharField(max_length=200)
    dni = forms.CharField(max_length=200)

class CrearTarea2 (forms.ModelForm): #Esta es otra manera de generar un formulario
    class Meta:
        model = Task2
        fields = ['title', 'descripcion', 'important']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la tarea'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control','placeholder': 'Descripción de la tarea'}),
            'important': forms.CheckboxInput(attrs={'class': 'form-check-input m-auto'}),
        }
