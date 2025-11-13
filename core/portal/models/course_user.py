from django.db import models
from django.utils.translation import gettext_lazy as _

from core.portal.models import Course
from core.authentication.models import User

class CourseUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='course_user')
    course = models.ForeignKey(Course, on_delete=models.PROTECT, related_name='course_user')
    initial_year = models.IntegerField(null=False, blank=False)
    final_year = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.user.name

    
    class Meta:
        db_table = 'course_user'
        verbose_name = _('course_user')
        verbose_name_plural = _('course_users')
        
        