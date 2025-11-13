from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from core.authentication.models import User
from core.authentication.serializers.user import UserListSerializer, UserDetailSerializer, UserWriteSerializer
from core.authentication.filters import UserFilter
from rest_framework_simplejwt.views import TokenObtainPairView
from core.authentication.serializers.user import CustomTokenObtainPairSerializer
from django_project.permission import UserCustomPermission
from django_filters.rest_framework import DjangoFilterBackend

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = UserFilter

    def get_serializer_class(self):
        if self.action == 'list':
            return UserListSerializer
        if self.action == 'retrieve':
            return UserDetailSerializer
        return UserWriteSerializer