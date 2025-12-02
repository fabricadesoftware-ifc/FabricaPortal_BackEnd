from rest_framework.routers import DefaultRouter


from core.portal.views import AccessViewSet, AreaViewSet, CourseUserViewSet, CourseViewSet, UserTagViewSet, ProjectViewSet, NewViewSet, TagViewSet

portal_router = DefaultRouter()
portal_router.register(r'access', AccessViewSet)
portal_router.register(r'areas', AreaViewSet)
portal_router.register(r'courses', CourseViewSet)
portal_router.register(r'course_users', CourseUserViewSet)
portal_router.register(r'user_tags', UserTagViewSet)
portal_router.register(r'projects', ProjectViewSet)
portal_router.register(r'news', NewViewSet)
portal_router.register(r'tags', TagViewSet)
