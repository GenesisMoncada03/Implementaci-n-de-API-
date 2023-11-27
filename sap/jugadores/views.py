from django.shortcuts import render
# Create your views here.
from django.forms import modelform_factory
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from jugadores.forms import JugadorFormulario
from jugadores.models import Jugador
# Create your views here.
#JugadorFormulario = modelform_factory(Jugador, exclude=['activo',])
def agregar_jugador(request):
    pagina = loader.get_template('agregar_jugador.html')
    if request.method == 'GET':
        formulario = JugadorFormulario
    elif request.method == 'POST':
        formulario = JugadorFormulario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('jugadores')
    datos = {'formulario':formulario}
    return HttpResponse(pagina.render(datos,request))

def modificar_jugador(request, jugador_id):
    pagina = loader.get_template('modificar_jugador.html')
    jugador = get_object_or_404(Jugador, pk=jugador_id)
    if request.method == 'GET':
        formulario = JugadorFormulario(instance=jugador)
    elif request.method == 'POST':
        formulario = JugadorFormulario(request.POST, instance=jugador)
        if formulario.is_valid():
            formulario.save()
            return redirect('jugadores')
    datos = {'formulario': formulario}
    return HttpResponse(pagina.render(datos, request))

def ver_jugador(request, jugador_id):
    # jugadores = jugadores.objects.get(pk=id)
    jugador = get_object_or_404(Jugador, pk=jugador_id)
    datos = {'jugador':jugador}
    #print(jugador)
    pagina = loader.get_template('ver_jugador.html')
    return HttpResponse(pagina.render(datos, request))

def eliminar_jugador(request, jugador_id):
    jugador = get_object_or_404(Jugador, pk=jugador_id)
    if jugador:
        jugador.delete()
        return redirect('jugadores')
