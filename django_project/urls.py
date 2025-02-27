from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

from django_project.router import router

from core.authentication.utils.verify_user_view import VerifyUserView

urlpatterns = [
    path('', RedirectView.as_view(url='/api/', permanent=True)),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/verify-user/', VerifyUserView.as_view(), name='verify_user')
]
