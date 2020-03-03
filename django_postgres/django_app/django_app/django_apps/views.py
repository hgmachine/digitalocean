from django.shortcuts import render
from django_apps.models import Pessoa
from django.http import HttpResponse

def index(request):
    """Diga alô a pessoa mais velha"""
    pessoas= Pessoa.objects.order_by('idade')
    pessoa= pessoas.last()
    if pessoa == None:
        tag= "Eu sou a pessoa mais velha aqui."
    else:
        tag= "Olá " + str(pessoa) + ", você é a pessoa mais velha."
    return HttpResponse(tag)

def show(request):
    """Carrega uma página semi-estática"""
    pessoas= Pessoa.objects.order_by('idade')
    content= {'pessoas': pessoas}
    return render(request,'django_apps/people.html', content)
