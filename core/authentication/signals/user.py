from django.db.models.signals import post_save
from django.dispatch import receiver
import logging

from core.authentication.models import User
from core.authentication.utils.verify import Verify

logger = logging.getLogger(__name__)

@receiver(post_save, sender=User)
def send_verification_email_signal(sender, instance, created, **kwargs):
    try:
        logger.info('Tentando enviar código de verificação')
        print(f"Signal ativado para usuário {instance.email}, created={created}")
        
        if created:
            code = Verify.send_code('fabio.moura@ifc.edu.br')
            print(f"Código de verificação enviado: {code}")
            
        logger.info(f'Código de verificação enviado para {instance.email}')
    except Exception as e:
        logger.error(f'Erro ao enviar código de verificação: {str(e)}')
        print(f'Erro ao enviar código de verificação: {str(e)}')


