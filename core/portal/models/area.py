from django.db import models
from django.utils.translation import gettext_lazy as _

from core.portal.models import Course

class Area(models.Model):
    name = models.CharField(max_length=255)
    course = models.ForeignKey(Course, on_delete=models.PROTECT, related_name='area')
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'area'
        verbose_name = _('area')
        verbose_name_plural = _('areas')
        
        