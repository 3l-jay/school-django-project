from django import forms
from . import models


class CreateArticle(forms.ModelForm):
    """
    Form class for creating an article.

    This class defines a form for creating an article using the Article model.
    It specifies the fields to be included in the form.

    Attributes:
        model (class): The model class for which the form is created, which is Article.
        fields (list): The list of fields from the model to include in the form,
                       including 'title', 'slug', 'body', and 'author'.
    """
    class Meta:
        model = models.Article
        fields = ['title', 'slug', 'body', 'author']
