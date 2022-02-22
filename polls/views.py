from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question
# Create your views here.

def index(request):                                                                     #Vista basada en Funcion recibe request
    lastest_quiestion_list = Question.objects.all()
    return render(request, "polls/index.html", 
                  {"lastest_quiestion_list": lastest_quiestion_list})           #responde con un http


def detail(request, question_id):
    question =  get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question" : question})

def resoult(request, question_id):
    return HttpResponse(f"Estas viendo los resultados de la pregunta No {question_id}")

def vote(request, question_id):
    return HttpResponse(f"Estas votando por la pregunta No {question_id}")