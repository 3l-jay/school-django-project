"""
Django AppConfig Documentation

This AppConfig class defines configuration for the 'artists' Django app.

Attributes:
    default_auto_field: Specifies the type of primary key used in models. 
                        Uses 'django.db.models.BigAutoField' by default.
    name: Specifies the name of the Django app, in this case, 'artists'.
"""

from django.apps import AppConfig


class ArtistsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'artists'
