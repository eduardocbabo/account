# from django.db.models.signals import post_save, post_delete
# from django.dispatch import receiver
# from django.contrib.auth.models import User
# from .models import Profile

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         # Cria o Profile com is_active=False
#         Profile.objects.create(user=instance, first_name=instance.first_name, last_name=instance.last_name, email=instance.email)
#         # Define is_active como False para o User
#         instance.is_active = False
#         instance.save()

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     # Este sinal é chamado sempre que um User é salvo
#     # Atualiza os dados do Profile associado ao User
#     if hasattr(instance, 'profile'):
#         profile = instance.profile
#         profile.first_name = instance.first_name
#         profile.last_name = instance.last_name
#         profile.email = instance.email
#         profile.save()

# @receiver(post_delete, sender=User)
# def delete_user_profile(sender, instance, **kwargs):
#     try:
#         instance.profile.delete()  # Tenta deletar o Profile associado
#     except Profile.DoesNotExist:
#         pass

# @receiver(post_save, sender=Profile)
# def update_user_from_profile(sender, instance, created, **kwargs):
#     if not created:  # Verifica se o Profile foi atualizado
#         user = instance.user
#         # Verifica se os dados do usuário precisam ser atualizados
#         if (user.first_name != instance.first_name or 
#             user.last_name != instance.last_name or 
#             user.email != instance.email):
#             user.first_name = instance.first_name
#             user.last_name = instance.last_name
#             user.email = instance.email
#             user.save(update_fields=['first_name', 'last_name', 'email'])


# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.contrib.auth import get_user_model

# User = get_user_model()

# @receiver(post_save, sender=User)
# def set_user_email(sender, instance, created, **kwargs):
#     if created:
#         # Verifica se o email já está definido, se não, define-o como o email do usuário
#         if not instance.email:
#             instance.email = instance.username  # Supondo que o username é o e-mail
#             instance.save()




from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from allauth.account.models import EmailAddress  # Usando modelo do Allauth
from django.core.exceptions import ValidationError
from .models import Profile

@receiver(post_save, sender=User)
def create_user_email(sender, instance, created, **kwargs):
    if created:
        # Verificar se o e-mail está presente
        if instance.email:
            EmailAddress.objects.create(
                user=instance,
                email=instance.email,
                verified=False,
                primary=True
        )

        print(f"E-mail registrado: {instance.email} para o usuário: {instance.username}")

    Profile.objects.get_or_create(user=instance)
    print(f"Profile criado para o usuário: {instance.username}")




@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    # Atualiza o Profile se o User já existir
    if hasattr(instance, 'profile'):
        instance.profile.first_name = instance.first_name
        instance.profile.last_name = instance.last_name
        instance.profile.save()
        print(f"Profile atualizado para o usuário: {instance.username}")

@receiver(post_delete, sender=User)
def delete_user_email(sender, instance, **kwargs):
    # Delete o EmailAddress quando o User for deletado
    EmailAddress.objects.filter(user=instance).delete()
    print(f"E-mail deletado para o usuário: {instance.username}")

    # Delete o Profile quando o User for deletado
    if hasattr(instance, 'profile'):
        instance.profile.delete()
        print(f"Profile deletado para o usuário: {instance.username}")