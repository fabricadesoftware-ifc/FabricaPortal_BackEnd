from django.db import models
from django.utils.translation import gettext_lazy as _

from core.portal.models.tag import Tag

class Access(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.PROTECT, related_name='tag')
    class Status(models.IntegerChoices):
        AUTORIZADO = 1, 'Autorizado'
        NAO_AUTORIZADO = 2, 'Não autorizado'
        NAO_CADASTRADO = 3, 'Não cadastrado'
    status = models.IntegerField(choices=Status.choices)
    class Type(models.IntegerChoices):
        TAG = 1, 'Tag'
        APP = 2, 'App'
    type = models.IntegerField(choices=Type.choices)

    def __str__(self):
        return self.tag.rfid
    
    class Meta:
        db_table = 'access'
        verbose_name = _('access')
        verbose_name_plural = _('access')