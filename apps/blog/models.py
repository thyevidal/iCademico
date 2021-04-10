from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.
class Blog(models.Model):
    autor = models.CharField('Autor', max_length=100)
    titulo = models.CharField('Titulo', max_length=200)
    slug = models.SlugField('Atalho')
    texte = models.TextField('Texto')
    imagem = models.ImageField(upload_to='blog/images', verbose_name='Imagem', null= True, blank=True)
    criacaodata = models.DateTimeField(default =timezone.now)
    publidata = models.DateTimeField(default =timezone.now)

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('blog:details' , args=[str(self.slug)])