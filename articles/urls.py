"""
Django URL Patterns Documentation

These URL patterns define routes for accessing different views related to articles in a Django app.

Attributes:
    app_name: Specifies the namespace for the app, in this case, 'articles'.
    urlpatterns: List of URL patterns.

URL Patterns:
    '' (empty path): Maps to the article_list view. URL name: 'list'.
    'create/': Maps to the article_create view. URL name: 'create'.
    '<slug:slug>/': Maps to the article_detail view, expecting a slug parameter. URL name: 'detail'.
"""

from django.urls import path
from .import views

app_name = 'articles'
urlpatterns = [
    path('', views.article_list, name='list'),
    path('create/', views.article_create, name='create'),
    path('<slug:slug>/', views.article_detail, name='detail'),
]
