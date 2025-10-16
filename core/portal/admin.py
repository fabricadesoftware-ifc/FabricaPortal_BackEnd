from django.contrib import admin

from core.portal.models import Project, Area, Course, CourseMember, Member, New, Tag, Access, MembrerTag

# Register your models here.
admin.site.register(Project)
admin.site.register(Area)
admin.site.register(Course)
admin.site.register(CourseMember)
admin.site.register(Member)
admin.site.register(New)
admin.site.register(Tag)
admin.site.register(Access)
admin.site.register(MembrerTag)
