from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', views.home, name="home"),
    path('pricing', views.pricing_view, name="pricing"),
    path('about', views.about, name="about"),
    path('faq', views.faq, name="faq"),
    path('contact', views.contact, name="contact"),
    path('login', auth_view.LoginView.as_view(template_name='login.html'), name="login"),
    path('logout', auth_view.LogoutView.as_view(template_name='logout.html'), name="logout"),
    path('signup', views.signup, name="signup"),
    path('profile', views.profile, name="profile"),
    path('privacy', views.privacy, name="privacy"),
]
