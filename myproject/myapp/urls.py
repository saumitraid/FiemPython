from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home-page'),
    path('about', views.about, name='about-page'),
    path('signup/', views.signUp, name='signup-page'),
    path('signin/', views.signin, name='signin-page'),
    path('allprod/', views.displayProduct, name='prod-page'),
    path('signout/', views.signOut, name='signout-page'),
    path('add_to_cart/<int:p_id>/', views.add_to_cart, name='adddcart-page'),
    path('allcart/', views.viewCart, name='vcart-page'),
    path('remove/<int:id>/', views.remove_cart, name='remcart-page'),
    path("initiate-payment/", views.initiate_payment, name="initiate_payment"),
    path("payment-success/", views.payment_success, name="payment_success"),
    path("payment-failed/", views.payment_failed, name="payment_failed"),
]
