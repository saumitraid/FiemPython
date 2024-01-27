from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home-page'),
    path('about', views.about, name='about-page'),
    path('signup', views.signUp, name='signup-page'),
    path('signin', views.signin, name='signin-page'),
    path('allprod', views.displayProduct, name='prod-page'),
]
