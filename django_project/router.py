from rest_framework.routers import DefaultRouter

from core.portal.router import portal_router
from core.uploader.router import uploader_router

router = DefaultRouter()
router.registry.extend(portal_router.registry)
router.registry.extend(uploader_router.registry)
