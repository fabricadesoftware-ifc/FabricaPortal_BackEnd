from django.db import models
from django.utils.translation import gettext_lazy as _

from core.portal.models.member import Member
from core.portal.models.tag import Tag

class MembrerTag(models.Model):
    member = models.ForeignKey(Member, on_delete=models.PROTECT, related_name='member_tag')
    tag = models.ForeignKey(Tag, on_delete=models.PROTECT, related_name='member_tag')
    initial_date = models.DateField(null=False, blank=False)
    final_date = models.DateField(null=False, blank=False)

    def __str__(self):
        return f'{self.member.name} - {self.tag.rfid}'
    
    class Meta:
        db_table = 'member_tag'
        verbose_name = _ ('member_tag')
        verbose_name_plural = _ ('member_tags')