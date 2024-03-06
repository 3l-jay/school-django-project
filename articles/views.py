"""
Django Views Documentation

These views handle HTTP requests related to articles in a Django app.

Functions:
    article_list(request): Renders a list of all articles sorted by date.
    article_detail(request, slug): Renders the details of a specific article identified by its slug.
    article_create(request): Renders a form to create a new article. If form data is submitted, validates and saves the article.
                              Requires user authentication; redirects to login page if user is not authenticated.

Dependencies:
    render: Renders HTML templates.
    redirect: Redirects to a specified URL.
    Article: Model representing an article (imported from .models).
    login_required: Decorator to ensure user authentication.
    forms: Module containing form classes (imported from .).
"""

from django.shortcuts import render, redirect
from .models import Article
from django.contrib.auth.decorators import login_required
from . import forms


# Create your views here.
def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/article_list.html', {'articles': articles})


def article_detail(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/article_detail.html', {'article': article})


@login_required(login_url='/accounts/login/')
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('articles:list')
    else:
        form = forms.CreateArticle()
    return render(request, 'articles/article_create.html', {'form': form})
