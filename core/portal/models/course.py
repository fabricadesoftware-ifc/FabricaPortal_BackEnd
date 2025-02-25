from django.db import models
from django.utils.translation import gettext_lazy as _

class Course(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'course'
        verbose_name = _('course')
        verbose_name_plural = _('courses')
        
        