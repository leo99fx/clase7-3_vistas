from django.http import HttpResponse
import random
from datetime import datetime
from django.shortcuts import render
from django.template import Context, Template, loader

def inicio(request):
    # return HttpResponse("Hola soy la nueva pagina")
    return render(request, "indice/index.html",{})

def otra_vista(request):
    return HttpResponse('''
                        <h1> Este es un titulo en h1</h1>
                        ''')

def numero_random(request):
    numero=random.randrange(0,11)
    texto=f'<h1>Este es tu numero random: {numero}</h1>'
    return HttpResponse(texto)

def numero_usuario(request, numero):
    texto=f'<h1>Su numero de usuario es: {numero}</h1>'
    return HttpResponse(texto)

def cumpleaños(request, año):
    now=datetime.now()
    año_hoy=now.year
    edad=año_hoy-año
    return HttpResponse(edad)

def mi_plantilla(request):
    
    # # template=loader.get_template("mi_plantilla.html")

    

    nombre='Jorge'
    apellido='Atahualpa'

    lista=[23,451,5,5,643,12]

    diccionario_de_datos={
        'nombre': nombre,
        'apellido': apellido,
        'nombre_largo': len(nombre),
        'lista': lista
    }
    

    # version vieja con open
    # plantilla=open("D:/06) Documentos, Musica, Fotos y Videos_backup/Cursos/Python/Programas/clase16/test_proyecto/plantillas/mi_plantilla.html")
    # template=Template(plantilla.read())
    # plantilla.close()
    # context= Context(diccionario_de_datos)
    # plantilla_preparada=template.render(dicionarrio_de_datos)

    # version nueva con loader
    # template=loader.get_template("mi_plantilla.html")
    # plantilla_preparada=template.render(diccionario_de_datos) #antes le pasa el context
    # return HttpResponse(plantilla_preparada)

    return render(request, "indice/mi_plantilla.html", diccionario_de_datos)