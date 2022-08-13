from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from AppCoder.models import Estudiantes


def estudiantes(request, nombre, apellido, email):
    alumno = Estudiantes(nombre=nombre, apellido=apellido, email=email)
    alumno.save()
    plantilla = loader.get_template('Estudiantes.html')

    contexto = {
        "nombre": alumno.nombre,
        "apellido": alumno.apellido,
        "email": alumno.email,
    }

    documento = plantilla.render(contexto)

    return HttpResponse(documento)

