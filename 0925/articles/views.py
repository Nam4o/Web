from django.shortcuts import render
from .models import Articles

# Create your views here.

def index(request):
    articles = Articles.objects.all()
    context = {
        'articles' : articles
    }
    
    return render(request, 'articles/index.html', context)