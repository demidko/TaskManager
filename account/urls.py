#from django.conf.urls import url
from . import views
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    #path('login/', views.user_login, name='login'),
    path('', views.dashboard, name='dashboard'),
    # login/logout
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('logout-then-login/', auth_views.logout_then_login, name='logout_then_login'),
    # change password
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    # restore password
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    # register
    path('register/', views.register, name='register'),
]