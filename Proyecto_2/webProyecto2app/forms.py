from django.forms import ModelForm, EmailInput

from webProyecto2app.models import Alumno, Calificaciones


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

