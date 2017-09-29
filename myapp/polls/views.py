from django.http import HttpResponse # codigo agregado
from django.shortcuts import render
from .models import Preguntas # codigo agregado para preguntas

# Create your views here. Jvillagran: se creo nuevo codigo
def index(request):
    return HttpResponse("Hola Mundo")

# Jvillagran: se creo nueva funcion para Preguntas.html
def preguntas(request):
    preguntas = Preguntas.objects.all()
    context = {'preguntas': preguntas}
    return render(request, 'preguntas.html', context)
