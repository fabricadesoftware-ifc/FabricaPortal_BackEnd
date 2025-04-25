from django.db import models
from django.utils.translation import gettext_lazy as _

from core.portal.models import Course, Member

class CourseMember(models.Model):
    member = models.ForeignKey(Member, on_delete=models.PROTECT, related_name='course_member')
    course = models.ForeignKey(Course, on_delete=models.PROTECT, related_name='course_member')
    initial_year = models.IntegerField(null=False, blank=False)
    final_year = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.member.name

    
    class Meta:
        db_table = 'course_member'
        verbose_name = _('course_member')
        verbose_name_plural = _('course_members')
        
        