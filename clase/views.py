from django.http import HttpResponse
from django.shortcuts import render
from clase.models import Curso
import random
# Create your views here.

def nuevo_curso(request):
    camada=random.randrange(500,3000)
    nuevo_curso=Curso(nombre= 'Curso Python', camada='13414') 
    nuevo_curso.save()
    return HttpResponse(f' Se creo el curso {nuevo_curso.nombre}, cada {nuevo_curso.camada}')