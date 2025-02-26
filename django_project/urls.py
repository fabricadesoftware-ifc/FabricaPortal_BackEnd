from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

from django_project.router import router

urlpatterns = [
    path('', RedirectView.as_view(url='/api/', permanent=True)),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
