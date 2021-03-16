from django.urls import path, include
from . import views

app_name="mainapp"
urlpatterns = [
    path('', views.index, name='index'),
    path('details/<int:id>/', views.details, name='details'),
    path('about/', views.about, name='about'),
    path('board/', views.board, name='board'),
    path('information/', views.information, name='information'),
    path('training/', views.training, name='training'),
    path('research/', views.research, name='research'),
    path('finance/', views.finance, name='finance'),
    path('kenya/', views.kenya, name='kenya'),
    path('tanzania/', views.tanzania, name='tanzania'),
    path('uganda/', views.uganda, name='uganda'),
    path('privacy/', views.privacy, name='privacy'),
    path('adverts/', views.advert, name='advert'),





]
