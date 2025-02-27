from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from core.authentication.models import User


class VerifyUserView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            email = request.query_params.get('email')
            code = request.query_params.get('code')
            user = User.objects.get(email=email)
            if user is None:
                return Response({'message': 'Usuário não encontrado'}, status=status.HTTP_404_NOT_FOUND)
            if user.verification_code != code:
                return Response({'message': 'Código inválido'}, status=status.HTTP_400_BAD_REQUEST)
            elif user.verification_code == code and user.is_verified:
                return Response({'message': 'Usuário já verificado'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                user.is_verified = True
                user.save()
                return Response({'message': 'Usuário verificado com sucesso'}, status=status.HTTP_200_OK)
            
        except User.DoesNotExist:
            return Response({'message': 'Usuário não encontrado'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)