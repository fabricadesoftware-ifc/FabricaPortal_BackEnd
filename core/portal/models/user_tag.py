from django.db import models
from django.utils.translation import gettext_lazy as _

from core.authentication.models import User
from core.portal.models.tag import Tag

class UserTag(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='user_tag')
    tag = models.ForeignKey(Tag, on_delete=models.PROTECT, related_name='user_tag')
    initial_date = models.DateField(null=False, blank=False)
    final_date = models.DateField(null=False, blank=False)

    def __str__(self):
        return f'{self.user.name} - {self.tag.rfid}'
    
    class Meta:
        db_table = 'user_tag'
        verbose_name = _ ('user_tag')
        verbose_name_plural = _ ('user_tags')