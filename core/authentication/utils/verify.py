from core.authentication.models import User
from core.authentication.utils.mail import send_verification_code
from rest_framework import response, status
import secrets
import logging

logger = logging.getLogger(__name__)

class Verify:
    def send_code(id):
        try:
            code = str(secrets.randbelow(900000) + 100000)
            try:
                user = User.objects.get(id=id)
                userid = user.id
                user.verification_code = code
                user.save()
                send_verification_code(userid, code)
            except Exception as e:
                return logging.error('Erro ao enviar código de verificação', e)
            
        except Exception:
            return logging.error('Erro ao enviar código de verificação', )
