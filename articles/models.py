"""
Django Models Documentation

These models represent articles in a Django app.

Model:
    Article: Represents an article with various fields.

Attributes:
    id: Auto-incrementing primary key.
    title: CharField for the title of the article.
    slug: SlugField for a unique URL-friendly identifier.
    body: TextField for the content of the article.
    author: ForeignKey to the User model representing the author of the article.
    date: DateTimeField representing the date and time when the article was created.

Methods:
    __str__(): Returns the title of the article as a string.
    snippet(): Returns the first 50 characters of the article's body followed by '...'.

Dependencies:
    models: Module containing Django model classes.
    User: Model representing a user (imported from django.contrib.auth.models).
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# required fields to complete a article.
class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    # show only first 50 characters of article.
    def snippet(self):
        return self.body[:50] + '...'
