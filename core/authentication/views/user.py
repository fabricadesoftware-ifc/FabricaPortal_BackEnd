from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from core.authentication.models import User
from core.authentication.serializers import UserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from core.authentication.serializers.user import CustomTokenObtainPairSerializer

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['email', 'name']
    ordering_fields = ['email', 'name', 'date_joined', 'last_login']
    ordering = ['email']