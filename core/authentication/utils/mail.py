import os
from django.core.mail import send_mail
from django_project.settings import EMAIL_HOST_USER, BASE_DIR
from django.utils.html import strip_tags
import logging

logger = logging.getLogger(__name__)

def send_verification_code(email, code):
    try:
        subject = 'Verificação de conta'
        message = f'Seu código de verificação é: {code}'
        from_email = EMAIL_HOST_USER
        recipient_list = [email]
        
        print(f"Tentando enviar email para {email} com código {code}")
        
        result = send_mail(
            subject=subject,
            message=message,
            from_email=from_email,
            recipient_list=recipient_list,
            fail_silently=False,
        )
        
        if result:
            logger.info(f"Email enviado com sucesso para {email}")
            print(f"Email enviado com sucesso para {email}")
            return True
        else:
            logger.error(f"Falha ao enviar email para {email}")
            print(f"Falha ao enviar email para {email}")
            return False
            
    except Exception as e:
        logger.error(f"Erro ao enviar email: {str(e)}")
        print(f"Erro ao enviar email: {str(e)}")
        return False