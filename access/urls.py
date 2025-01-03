from django.urls import path
from . import views
from .views import criar_profile
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('auth/user/<int:user_id>/send_email/', views.send_email_view, name='admin_send_email'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    path('plataforma/', views.plataforma, name='plataforma'),
    path('criar_profile/', criar_profile, name='criar_profile'),
    path('admin/password_reset/', auth_views.PasswordResetView.as_view(), name='admin_password_reset'),
]