from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from core.authentication.managers import CustomUserManager
from core.uploader.models import Image

class User(AbstractUser):
    class TypeChoices(models.TextChoices):
        DOCENTE = 'Docente'
        DISCENTE = 'Discente'
        TAE = 'TAE'
        EXTERNO = 'Externo'
    
    class StateChoices(models.TextChoices):
        ATIVO = 'Ativo'
        INATIVO = 'Inativo'
        EGRESSO = 'Egresso'
    
    username = None
    email = models.EmailField(_('email address'), unique=True)
    password = models.CharField(_('password'), max_length=128)
    name = models.CharField(_('name'), max_length=150)
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
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    last_login = models.DateTimeField(_('last login'), auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def save(self, *args, **kwargs):
        if not self.password.startswith('pbkdf2_sha256$'):
            self.set_password(self.password)
        super().save(*args, **kwargs)

    objects = CustomUserManager() # type: ignore

    def __str__(self):
        return self.email
    
    class Meta:
        db_table = 'user'
        verbose_name = _('user')
        verbose_name_plural = _('users')
