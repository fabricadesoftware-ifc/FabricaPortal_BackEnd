from django.db import models
from django.utils.translation import gettext_lazy as _
from core.uploader.models import Image

class Member(models.Model):
    class TypeChoices(models.TextChoices):
        DOCENTE = 'Docente'
        DISCENTE = 'Discente'
        TAE = 'TAE'
        EXTERNO = 'Externo'
        
    class StateChoices(models.TextChoices):
        ATIVO = 'Ativo'
        INATIVO = 'Inativo'
        EGRESSO = 'Egresso'
    
    name = models.CharField(max_length=255)
    linkedin = models.URLField(max_length=255, null=True, blank=True)
    github = models.URLField(max_length=255, null=True, blank=True)
    instagram = models.URLField(max_length=255, null=True, blank=True)
    type = models.CharField(max_length=20, choices=TypeChoices)
    status = models.CharField(max_length=20, choices=StateChoices)
    biography = models.TextField()
    image = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
    )
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'member'
        verbose_name = _('member')
        verbose_name_plural = _('members')
        
        