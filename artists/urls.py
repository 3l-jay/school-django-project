from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('', views.home, name='K.Dot-home'),
    path('catalogue/', views.catalogue),
]
