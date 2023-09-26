from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


# def new(request):
#     form = ArticleForm()
#     context = {
#         'form': form,
#     }
#     return render(request, 'articles/new.html', context)


def create(request):
    # 요청의 메서드가 POST 라면
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    
    # 요청의 메서드가 POST 가 아니라면 (new)
    else:
        form = ArticleForm()
    context = {
        'form': form
    }

    return render(request, 'articles/create.html', context)

    # form = ArticleForm(request.POST)
    # # 유효성 검사 진행
    # if form.is_valid():
    #     # 유효성 검사가 통과된 경우
    #     article = form.save()
    #     return redirect('articles:detail', article.pk)
    # context = {
    #     'form': form,
    # }
    # return render(request, 'articles/new.html', context)

    # # title = request.POST.get('title')
    # # content = request.POST.get('content')
    # article = Article(title=title, content=content)
    # article.save()
    # return redirect('articles:index')


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')


def edit(request, pk):
    article = Article.objects.get(pk=pk)
    form = ArticleForm(instance=article)

    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/edit.html', context)


def update(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == 'POST':    
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid:
            form.save()
            return redirect('articles:detail', article.pk)
        context = {
            'form': form,
    }    

    # article.title = request.POST.get('title')
    # article.content = request.POST.get('content')
    # article.save()
        return redirect('articles:detail', context)
    else:
        form = ArticleForm(instance=article)
        context = {
            'article': article,
            'form': form,
        }
        return render(request, 'articles/update.html', context)