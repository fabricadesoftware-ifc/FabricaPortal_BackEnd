from core.authentication.models import User
from core.authentication.utils.mail import send_verification_code
from rest_framework import response, status
import secrets
import logging

logger = logging.getLogger(__name__)

class Verify:
    @staticmethod
    def verify_user(email, code):
        try:
            user = User.objects.get(email=email)
            if user.verification_code == code:
                user.is_verified = True
                user.save()
                return True
            return False
        except User.DoesNotExist:
            return False
    
    @staticmethod
    def verify_email(email):
        try:
            return True #email.endswith('@ifc.edu.br')
        except:
            return False
    
    @staticmethod
    def send_code(email):
        try:
            code = str(secrets.randbelow(900000) + 100000)
            if Verify.verify_email(email) == False:
                return response.Response({'message': 'Email não autorizado'}, status=status.HTTP_400_BAD_REQUEST)
            
            try:
                user = User.objects.get(email=email)
                user.verification_code = code
                user.save()
                send_verification_code(email, code)
            except User.DoesNotExist:
                User.objects.create(email=email, verification_code=code)
                
            return code
            
        except Exception:
            return logging.error('Erro ao enviar código de verificação', )
