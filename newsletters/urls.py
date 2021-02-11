#from django.conf.urls import url
from django.urls import path, include
#from . import views
from .views import newsletter_signup, newsletter_unsubscribe

app_name="newsletter"
urlpatterns = [
    path('sign_up/', newsletter_signup, name='newsletter_signup'),
    path('unsubscribe/', newsletter_unsubscribe, name='newsletter_unsubscribe'),
]
