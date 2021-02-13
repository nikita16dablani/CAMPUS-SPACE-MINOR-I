from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('team',views.team,name='team'),
    path('login',views.user_login,name='login'),
    path('register',views.register,name='register'),
    path('contact',views.contact,name='contact'),
    path('bullet', views.bullet, name='bullet'),
    path('logout', views.user_logout, name='logout'),
    path('notes', views.notes, name='notes'),
    path('notice', views.notice, name='notice'),

]