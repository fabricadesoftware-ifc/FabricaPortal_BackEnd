from django.db import models
from django.utils.translation import gettext_lazy as _

class Tag(models.Model):
    rfid = models.CharField(max_length=10)

    def __str__(self):
        return self.rfid
    
    class Meta:
        db_table = 'tag'
        verbose_name = _('tag')
        verbose_name_plural = _('tags')