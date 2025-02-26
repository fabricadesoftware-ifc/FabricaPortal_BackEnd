from django.contrib import admin
from django.urls import path, include
from core.authentication.utils.verify_user_view import VerifyUserView
from django_project.router import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/verify-user/', VerifyUserView.as_view(), name='verify_user')
]
