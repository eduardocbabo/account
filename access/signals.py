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
            if not EmailAddress.objects.filter(email=instance.email).exists():
                EmailAddress.objects.create(
                    user=instance,
                    email=instance.email,
                    verified=False,
                    primary=True
                )

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