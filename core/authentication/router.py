from rest_framework.routers import DefaultRouter


from core.authentication.views import user

authentication_router = DefaultRouter()
authentication_router.register(r'users', user.UserViewSet)
