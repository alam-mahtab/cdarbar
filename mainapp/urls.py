from django.urls import path
from django.views.generic.base import TemplateView

from . import views
from django.contrib.auth import views as auth_views  # for password resetting

urlpatterns = [
    path('', views.film_festival, name='film-festival'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('signup_submission',views.signup_submission, name='signup_submission'),
   # path('forgetpassword', views.forgetpassword, name='forget-password'),
    path('schedule', views.schedule, name='schedule'),
    path('logout', views.logout, name='logout'),
    path('contact', views.contact, name='contact'),

    path('reset_password/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]