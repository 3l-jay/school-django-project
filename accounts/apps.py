from django.apps import AppConfig


class AccountsConfig(AppConfig):
    """
    AppConfig class for the 'accounts' app.

    This class defines the configuration for the 'accounts' app.
    It specifies the default auto-generated field for models and the name of the app.

    Attributes:
        default_auto_field (str): The name of the default auto-generated primary key field.
                                  By default, it is set to 'django.db.models.BigAutoField'.
        name (str): The name of the app, which is 'accounts'.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'
