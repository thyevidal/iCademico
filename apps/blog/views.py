from django.shortcuts import render
from .models import *
from django.db.models import Max

# Create your views here.
def index(request):
    context = {
        'post' : Blog.objects.all(),
        'sobre': Sobre.objects.last(),
        'faq': Faq.objects.all()[:3],
        'autore': Autore.objects.last(),
        'frase': Frase.objects.last(),
    }
    return render(request, 'index.html', context)
