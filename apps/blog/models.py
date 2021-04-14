from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.
class Blog(models.Model):
    autor = models.CharField('Autor', max_length=100)
    titulo = models.CharField('Titulo', max_length=200)
    slug = models.SlugField('Atalho')
    texto = models.TextField('Texto')
    imagem = models.ImageField(upload_to='media/blog-imagens', verbose_name='Imagem', null= True, blank=True)
    criacaodata = models.DateTimeField(default =timezone.now)
    publidata = models.DateTimeField(default =timezone.now)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('blog:details' , args=[str(self.slug)])

class Sobre(models.Model):
    titulo = models.CharField('Titulo', max_length=200)
    texto = models.TextField('Texto')

class Frase(models.Model):
    frase = models.CharField('Frase', max_length=200)

class Faq(models.Model):
    pergunta = models.CharField('Pergunta', max_length=200)
    resposta = models.TextField('Resposta')

class Autore(models.Model):
    nome = models.CharField('Nome', max_length=200)
    foto = models.ImageField(upload_to='media/blog-imagens/autores', verbose_name='Imagem', null= True, blank=True)
    likes = models.IntegerField(default=0)
    artigos = models.IntegerField(default=0)