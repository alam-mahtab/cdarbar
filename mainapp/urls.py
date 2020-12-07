from django.urls import path

from . import views

urlpatterns = [
    path('home', views.film_festival, name='film-festival'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('signup_submission',views.signup_submission, name='signup_submission'),
    path('forgetpassword', views.forgetpassword, name='forget-password'),
    path('schedule', views.schedule, name='schedule'),
    path('logout', views.logout, name='logout')
]