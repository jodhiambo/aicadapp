from django.urls import path, include
from . import views

app_name="facilities"
urlpatterns = [
    path('index', views.index, name='index')
]
