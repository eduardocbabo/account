# access/authentication_backend.py
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User

class EmailOrUsernameModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # Tenta autenticar com username
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            try:
                # Se não encontrar, tenta autenticar com email
                user = User.objects.get(email=username)
            except User.DoesNotExist:
                # Se não encontrar, retorna None
                return None
        
        # Verifica a senha
        if user.check_password(password):
            return user
        return None
