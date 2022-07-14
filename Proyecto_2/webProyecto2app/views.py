from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.forms import modelform_factory
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView


from webProyecto2app.forms import AlumnoForm, CalificacionesForm
from webProyecto2app.models import *


@login_required
def datosAlumnos(request):
    nro_alumnos = Alumno.objects.count()
    alumno = Alumno.objects.all()
    return render(request, 'datosAlumnos.html', {'nro_alumnos': nro_alumnos, 'alumno': alumno})

def datosCalificaciones(request):
    notas = Calificaciones.objects.all()
    return render(request, 'datosCalificaciones.html', { 'notas': notas})


def agregarAlumno(request):
    if request.method == 'POST':
        formaAlumno = AlumnoForm(request.POST)
        if formaAlumno.is_valid():
            formaAlumno.save()
            return redirect('listaDatosAlumnos')
    else:
        formaAlumno = AlumnoForm

    return render(request, 'nuevoalumno.html', {'formaAlumno': formaAlumno})



def editarAlumno(request, id):
    alumno = get_object_or_404(Alumno, pk=id)
    if request.method == 'POST':
        formaAlumno = AlumnoForm(request.POST, instance=alumno)
        if formaAlumno.is_valid():
            formaAlumno.save()
            return redirect('listaDatosAlumnos')
    else:
        formaAlumno = AlumnoForm(instance=alumno)
    return render(request, 'editar.html', {'formaAlumno': formaAlumno})


def editarCalificaciones(request, id):
    notas = get_object_or_404(Calificaciones, pk=id)
    if request.method == 'POST':
        formaCalifica = CalificacionesForm(request.POST, instance=notas)
        if formaCalifica.is_valid():
            formaCalifica.save()
            return redirect('enlaceDatosCalificaciones')
    else:
        formaCalifica = CalificacionesForm(instance=notas)
    return render(request, 'editarCalificaciones.html', {'formaCalifica': formaCalifica})


def eliminarAlumno(request, id):
    alumno = get_object_or_404(Alumno, pk=id)
    if alumno:
        alumno.delete()
    return redirect('listaDatosAlumnos')


def eliminarCalificaciones(request, id):
    notas = get_object_or_404(Calificaciones, pk=id)
    if notas:
        notas.delete()
    return redirect('enlaceDatosCalificaciones')


def agregarCalificaciones(request):
    if request.method == 'POST':
        formaCalificaciones = CalificacionesForm(request.POST)
        if formaCalificaciones.is_valid():
            formaCalificaciones.save()
            return redirect('enlaceDatosCalificaciones')
    else:
        formaCalificaciones = CalificacionesForm

    return render(request, 'nuevaCalificacion.html', {'formaCalificaciones': formaCalificaciones})


def salir(request):
    logout(request)
    return redirect('/')

# Create your views here.

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return redirect('/') #para que te lleve directamente a la vista seria la otra ruta ----listaDatosAlumnos
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request,'registration/registro.html',context)