from django.db import models

class Pessoa(models.Model):
    """Representação de uma pessoa com nome, idade e cpf"""
    nome= models.CharField(max_length=20)
    idade= models.CharField(max_length=10)
    cpf= models.CharField(max_length=15)

    def __str__(self):
        """Devolve o nome desta pessoa"""
        return self.nome
