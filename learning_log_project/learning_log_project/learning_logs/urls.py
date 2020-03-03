from . import views
from django.urls import path

urlpatterns = [
    # Página Inicial
    path('', views.index, name= 'index'),
    
    # Página pessoal
    path('pessoal/', views.showman, name='pessoal'),

    # Indice para notas de aula
    path('notes/', views.lessons, name='notes'),

    # Ementa de Integração e Testes
    path('integra_testes/', views.integra_testes, name='integra_testes'),

    # Ementa de Projeto de Estrutura de Veíulos
    path('proj_estrutura/', views.proj_estrutura, name='proj_estrutura'),

    # Notas de aulas
    path('lesson_1/', views.lesson_1, name='lesson_1'),

    # Mostra todos os assuntos
    path('topics/', views.topics, name='topics'), 
    
    # Página de detalhes para um único assunto
    path('topics/(?P<topic_id>\d+)/', views.topic, name='topic'),
    
    # Novo assunto
    path('new_topic/', views.new_topic, name='new_topic'),
    
    # Novo comentário
    path('new_entry/(?P<topic_id>\d+)/', views.new_entry, name='new_entry'),
    
    # Página para editar os assuntos já criados 
    path('edit_entry/(?P<entry_id>\d+)/', views.edit_entry, name='edit_entry'),
    
    # Deleta um assunto
    path('delete_entry/(?P<entry_id>\d+)/)', views.delete_entry, name='delete_entry'),
    
    # Deleta um topico
    path('delete_topic/(?P<topic_id>\d+)/)', views.delete_topic, name='delete_topic'),
]