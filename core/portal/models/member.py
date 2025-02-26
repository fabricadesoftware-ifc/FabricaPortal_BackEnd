from django.db import models
from django.utils.translation import gettext_lazy as _

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
    social_media = models.JSONField()
    type = models.CharField(max_length=20, choices=TypeChoices)
    status = models.CharField(max_length=20, choices=StateChoices)
    biography = models.TextField()
    #image = models.ImageField()
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'member'
        verbose_name = _('member')
        verbose_name_plural = _('members')
        
        