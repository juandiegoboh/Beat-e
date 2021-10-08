from django.urls import path
from App.views import *
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', LandingPage.as_view(), name='home'),
    path('signup', RegisterPage.as_view(), name='signup'),    
    path('favicon', RedirectView.as_view(url=staticfiles_storage.url('img/favicon.png')))
]