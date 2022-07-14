
from django.urls import path
from webProyecto2app.views import *
from django.contrib import admin

urlpatterns = [
    #path('', login, name='login'),
    path('', datosAlumnos, name='listaDatosAlumnos'), #rutaDatosAlumnos/
    path('rutaAregarAlumno/', agregarAlumno, name='agregarNuevo'),
    path('rutaEditarAlumno/<int:id>', editarAlumno, name='editarAlumno'),
    path('rutaEliminarAlumno/<int:id>', eliminarAlumno, name='eliminarAlumno'),
    path('rutaDatosCalificaciones/', datosCalificaciones, name='enlaceDatosCalificaciones'),
    path('rutaEditarCalificaciones/<int:id>', editarCalificaciones, name='enlaceEditarCalificaciones'),
    path('rutaEliminarCalificaciones/<int:id>', eliminarCalificaciones, name='enlaceEliminarCalificaciones'),
    path('rutaAgregarCalificaciones/', agregarCalificaciones, name='enlaceAgregarCalificaciones'),
    path('rutaRegistro/', registro, name='enlaceRegistro'),
    path('rutaSalir/', salir, name='enlaceSalir'),
]


