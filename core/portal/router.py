from rest_framework.routers import DefaultRouter


from core.portal.views import AreaViewSet, CourseMemberViewSet, CourseViewSet, MemberViewSet, ProjectViewSet, NewViewSet

portal_router = DefaultRouter()
portal_router.register(r'areas', AreaViewSet)
portal_router.register(r'courses', CourseViewSet)
portal_router.register(r'course_members', CourseMemberViewSet)
portal_router.register(r'members', MemberViewSet)
portal_router.register(r'projects', ProjectViewSet)
portal_router.register(r'news', NewViewSet)
