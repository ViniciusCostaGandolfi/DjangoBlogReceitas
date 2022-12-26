from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
import os


def mudarNomeImagem(instance, filename):
    filename = filename.split('.')
    data = str(datetime.now().date())
    microsecond = str(datetime.now().microsecond)
    filename = filename[-2] + microsecond + '.' + filename[-1]
    return os.path.join(f'fotos/{data}/', filename)

class Receita(models.Model):
    pessoa = models.ForeignKey(User, on_delete=models.CASCADE)
    nomeReceita = models.CharField(max_length=200)
    ingredientes = models.TextField()
    modoPreparo = models.TextField()
    tempoPreparo = models.IntegerField()
    rendimento = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    dataReceita = models.DateField(default=datetime.now, blank=True)
    publicada = models.BooleanField(default=False)
    fotoReceita = models.ImageField(upload_to=mudarNomeImagem, blank=True)

    def __str__(self):
        return self.nomeReceita
# Create your models here.


