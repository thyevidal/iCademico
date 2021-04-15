from django.shortcuts import render, get_object_or_404
from .models import *
from django.db.models import Max

# Create your views here.
def index(request):
    context = {
        'post' : Blog.objects.order_by('likes'),
        'sobre': Sobre.objects.last(),
        'faq': Faq.objects.all(),
        'autore': Autore.objects.all()[:3],
        'frase': Frase.objects.last(),
    }
    return render(request, 'index.html', context)

def blog(request, id_blog):
    post = {
        'chave': get_object_or_404(Blog, pk=id_blog),
    }
    return render(request, 'blog.html', post  )