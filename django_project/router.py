from rest_framework.routers import DefaultRouter

from core.portal.router import portal_router


router = DefaultRouter()
router.registry.extend(portal_router.registry)
