from django.db.models.signals import post_save
from django.dispatch import receiver
import logging

from core.authentication.models import User
from core.authentication.utils.verify import Verify

logger = logging.getLogger(__name__)

@receiver(post_save, sender=User)
def send_verification_email_signal(sender, instance, created, **kwargs):
    try:
        print(f"Signal ativado para usuário {instance.name}, created={created}")
        
        if created:
            Verify.send_code(instance.id)
            
    except Exception as e:
        print(f'Erro ao enviar verificação de conta: {str(e)}')


