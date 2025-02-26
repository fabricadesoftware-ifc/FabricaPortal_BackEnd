from rest_framework.routers import DefaultRouter

from core.portal.router import portal_router
from core.authentication.router import authentication_router


router = DefaultRouter()
router.registry.extend(portal_router.registry)
router.registry.extend(authentication_router.registry)
