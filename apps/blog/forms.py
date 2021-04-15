from django.forms import ModelForm
from .models import Blog, Sobre

class LikesBlogGet(ModelForm):
    class Meta:
        model = Blog
        fields = ['like']

class LikesSobreGet(ModelForm):
    class Meta:
        model = Sobre
        fields = ['like']