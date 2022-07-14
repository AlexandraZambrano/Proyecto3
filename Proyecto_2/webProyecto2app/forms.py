from django.forms import ModelForm, EmailInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from webProyecto2app.models import Alumno, Calificaciones
from django import forms



class AlumnoForm(ModelForm):
    class Meta:
        model = Alumno
        fields = '__all__'
        widgets = {
            'email': EmailInput(attrs={'type':'email'})
        }

class CalificacionesForm(ModelForm):
    class Meta:
        model = Calificaciones
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

