from django.contrib import admin

from core.portal.models import Project, Area, Course, CourseUser, New, Tag, Access, UserTag

# Register your models here.
admin.site.register(Project)
admin.site.register(Area)
admin.site.register(Course)
admin.site.register(CourseUser)
#admin.site.register(Member)
admin.site.register(New)
admin.site.register(Tag)
admin.site.register(Access)
admin.site.register(UserTag)
