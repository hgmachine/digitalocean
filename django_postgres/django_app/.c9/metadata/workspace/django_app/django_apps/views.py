{"filter":false,"title":"views.py","tooltip":"/django_app/django_apps/views.py","undoManager":{"mark":7,"position":7,"stack":[[{"start":{"row":2,"column":0},"end":{"row":2,"column":25},"action":"remove","lines":["# Create your views here."],"id":2},{"start":{"row":2,"column":0},"end":{"row":20,"column":56},"action":"insert","lines":["from django.shortcuts import render","from hwapps.models import Pessoa","from django.http import HttpResponse","","def index(request):","    \"\"\"Diga alô a pessoa mais velha\"\"\"","    pessoas= Pessoa.objects.order_by('idade')","    pessoa= pessoas.last()","    if pessoa == None:","        tag= \"Eu sou a pessoa mais velha aqui.\"","    else:","        tag= \"Olá \" + str(pessoa) + \", você é a pessoa mais velha.\"","    return HttpResponse(tag)","","def show(request):","    \"\"\"Carrega uma página semi-estática\"\"\"","    pessoas= Pessoa.objects.order_by('idade')","    content= {'pessoas': pessoas}","    return render(request,'hwapps/people.html', content)"]}],[{"start":{"row":1,"column":0},"end":{"row":2,"column":35},"action":"remove","lines":["","from django.shortcuts import render"],"id":4},{"start":{"row":1,"column":0},"end":{"row":2,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":18,"column":27},"end":{"row":18,"column":33},"action":"remove","lines":["hwapps"],"id":7},{"start":{"row":18,"column":27},"end":{"row":18,"column":28},"action":"insert","lines":["d"]},{"start":{"row":18,"column":28},"end":{"row":18,"column":29},"action":"insert","lines":["j"]},{"start":{"row":18,"column":29},"end":{"row":18,"column":30},"action":"insert","lines":["a"]},{"start":{"row":18,"column":30},"end":{"row":18,"column":31},"action":"insert","lines":["n"]},{"start":{"row":18,"column":31},"end":{"row":18,"column":32},"action":"insert","lines":["d"]}],[{"start":{"row":18,"column":31},"end":{"row":18,"column":32},"action":"remove","lines":["d"],"id":8}],[{"start":{"row":18,"column":31},"end":{"row":18,"column":32},"action":"insert","lines":["g"],"id":9},{"start":{"row":18,"column":32},"end":{"row":18,"column":33},"action":"insert","lines":["o"]}],[{"start":{"row":18,"column":27},"end":{"row":18,"column":33},"action":"remove","lines":["django"],"id":10},{"start":{"row":18,"column":27},"end":{"row":18,"column":38},"action":"insert","lines":["django_apps"]}],[{"start":{"row":1,"column":5},"end":{"row":1,"column":11},"action":"remove","lines":["hwapps"],"id":11},{"start":{"row":1,"column":5},"end":{"row":1,"column":6},"action":"insert","lines":["d"]},{"start":{"row":1,"column":6},"end":{"row":1,"column":7},"action":"insert","lines":["j"]},{"start":{"row":1,"column":7},"end":{"row":1,"column":8},"action":"insert","lines":["a"]},{"start":{"row":1,"column":8},"end":{"row":1,"column":9},"action":"insert","lines":["n"]}],[{"start":{"row":1,"column":5},"end":{"row":1,"column":9},"action":"remove","lines":["djan"],"id":12},{"start":{"row":1,"column":5},"end":{"row":1,"column":16},"action":"insert","lines":["django_apps"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":11,"column":22},"end":{"row":11,"column":22},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1570818149239,"hash":"f7a90573a443297abb1c7ce8cb52965a6a82be37"}