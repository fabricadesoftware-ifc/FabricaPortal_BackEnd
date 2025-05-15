from django.db import models
from django.utils.translation import gettext_lazy as _

from core.portal.models import Member, Area
from core.uploader.models import Image

class Project(models.Model):
    class StateChoices(models.TextChoices):
        NAO_INICIADO = 'Não Iniciado'
        DESENVOLVIMENTO = 'Em Desenvolvimento'
        CONCLUIDO = 'Concluído'
        CANCELADO = 'Cancelado'
    
    name = models.CharField(max_length=255)
    initial_date = models.DateField(auto_now_add=False)
    final_date = models.DateField(auto_now_add=False)
    technologies = models.ManyToManyField(Area)
    advisor = models.ForeignKey(Member, on_delete=models.PROTECT, related_name='advisor')
    members = models.ManyToManyField(Member)

    state = models.CharField(max_length=255, choices=StateChoices)
    images = models.ManyToManyField(
        Image,
        related_name="+",
        null=True,
        blank=True,
        default=None,
    )    
    links = models.JSONField()
    about = models.TextField()
    
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'project'
        verbose_name = _('project')
        verbose_name_plural = _('projects')
        
        