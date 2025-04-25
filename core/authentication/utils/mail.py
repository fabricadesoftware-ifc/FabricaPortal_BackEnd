import os
from django.conf import settings
from django.core.mail import send_mail
from django_project.settings import EMAIL_HOST_USER, BASE_DIR
from django.utils.html import strip_tags
import logging
from core.authentication.models import User
from django_project.celery import app

logger = logging.getLogger(__name__)

@app.task(queue="emails")
def send_verification_code(userid, code):
    try:
        user = User.objects.get(id=userid)
        print(userid)
        print(user.email)
        link = f'{settings.BASE_URL}verify-user?email={user.email}&code={code}'
        with open(os.path.join(BASE_DIR, 'core/authentication/templates/email.html'), 'r') as file:
            html = file.read()
            html = html.replace('link', link)
            html = html.replace('name', user.name)

        print(html)

        plain_message = strip_tags(html)
        from_email = EMAIL_HOST_USER
        recipient_list = settings.EMAIL_RECIPIENT
        
        result = send_mail(
            'Verificação de conta',
            plain_message,
            from_email=from_email,
            recipient_list=recipient_list,
            html_message=html
        )
        
        if result:
            logger.info(f"Email enviado com sucesso para {user.email}")
            print(f"Email enviado com sucesso para {user.email}")
            return True
        else:
            logger.error(f"Falha ao enviar email para {user.email}")
            print(f"Falha ao enviar email para {user.email}")
            return False
            
    except Exception as e:
        logger.error(f"Erro ao enviar email: {str(e)}")
        print(f"Erro ao enviar email: {str(e)}")
        return False