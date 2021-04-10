from django.shortcuts import render
from  .models import Blog

# Create your views here.
def index(request):
    context = {
        'post' : Blog.objects.all(),
    }
    return render(request, 'index.html', context)


