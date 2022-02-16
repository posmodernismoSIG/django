from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):                                                                     #Vista basada en Funcion recibe request
    return HttpResponse('Estas en la pagina principal de premios platzi app')           #responde con un http

def detail(request, question_id):
    return HttpResponse(f"Estas viendo la pregunta No {question_id}")

def resoult(request, question_id):
    return HttpResponse(f"Estas viendo los resultados de la pregunta No {question_id}")

def vote(request, question_id):
    return HttpResponse(f"Estas votando por la pregunta No {question_id}")