from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import render
from .models import Topic, Entry
from .forms import TopicForm, EntryForm

def index(request):
    """A página incial de Learning Log"""
    print("***************** HOME VIEW *****************")
    return render(request, 'learning_logs/index.html')

def showman(request):
    """Página com maiores informações pessoais"""
    return render(request,'learning_logs/pessoal.html')

def lessons(request):
    """Página de acesso aos complementos de aulas"""
    return render(request,'learning_logs/notes.html')

def lesson_1(request):
    """Página de acesso ao complemento de aula #1"""
    return render(request,'learning_logs/lesson_1.html')

def integra_testes(request):
    """Página de acesso ao complemento de aula #1"""
    return render(request,'learning_logs/integra_testes.html')
    
def proj_estrutura(request):
    """Página de acesso ao complemento de aula #1"""
    return render(request,'learning_logs/proj_estrutura.html')

@login_required    
def topics(request):
    """Mostra todos os assuntos"""
    topics = Topic.objects.order_by('date_added')
    # topics= Topic.objects.filter(owner=request.user).order_by('date_added')
    content = {'topics': topics}
    return render(request, 'learning_logs/topics.html', content)

@login_required      
def topic(request,topic_id):
    """Mostra um único assunto e todas as suas entradas"""
    topic= Topic.objects.get(id=topic_id)
    entries= topic.entry_set.order_by('date_added')
    context= {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html',context)

@login_required   
def new_topic(request):
    """Adicionando um novo assunto"""
    if request.method != 'POST':
        # Nenhum dado submetido; cria um formulário em branco
        form = TopicForm()
    else:
        # Dado de POST submetidos; processa os dados
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic= form.save(commit=False)
            new_topic.owner= request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))
    
    content = {'form': form}
    return render(request, 'learning_logs/new_topic.html', content)
    
@login_required       
def new_entry(request,topic_id):
    """Adicionando novo comentário"""
    topic = Topic.objects.get(id=topic_id)
    
    if request.method != 'POST':
        # Nenhum comentário submetido; cria um formulário em branco
        form = EntryForm()
    else:
        # Dados de POST submetidos; processa os dados
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry= form.save(commit=False)
            new_entry.topic= topic
            new_entry.owner= request.user
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id]))
    
    content = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', content)

@login_required   
def edit_entry(request,entry_id):
    """Edita uma entrada já criada"""
    entry= Entry.objects.get(id=entry_id)
    topic= entry.topic
    # Garante que o assunto oertence ao usuário atual
    if entry.owner!=request.user and request.user.id!=1:
        raise Http404

    if request.method != 'POST':
        # Requisição inicial preenche previamente o formulário com a entrada
        # atual
        form= EntryForm(instance=entry)
    else:
        # Dados de POST submetidos; processa os dados
        form= EntryForm(instance=entry, data=request.POST)
        if form.is_valid(): 
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic',args=[topic.id]))
    
    context= {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)

@login_required       
def delete_entry(request,entry_id):
    """Remove uma entrada"""
    # Garante que o assunto pertence ao usuário atual
    entry= Entry.objects.get(id=entry_id)
    if entry.owner!=request.user and request.user.id!=1:
        raise Http404
    
    topic= entry.topic
    Entry.objects.filter(id=entry_id).delete()
    entries= topic.entry_set.order_by('date_added')
    context= {'topic': topic, 'entries': entries}
    return render(request,'learning_logs/topic.html', context)

@login_required       
def delete_topic(request,topic_id): 
    """ Removendo um topico da lista """
    entries= Entry.objects.filter(topic_id=topic_id)
    for comment in entries:
        comment.delete()
        
    Topic.objects.filter(id=topic_id).delete()
    topics= Topic.objects.order_by('date_added')
    context= {'topics': topics}
    return render(request,'learning_logs/topics.html', context)
    
    