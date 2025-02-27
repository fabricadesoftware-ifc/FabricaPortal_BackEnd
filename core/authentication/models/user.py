from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from core.authentication.managers import CustomUserManager

class User(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    password = models.CharField(_('password'), max_length=128)
    name = models.CharField(_('name'), max_length=150)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    last_login = models.DateTimeField(_('last login'), auto_now=True)
    verification_code = models.CharField(_('verification code'), max_length=6, blank=True, null=True)
    is_verified = models.BooleanField(_('is verified'), default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def save(self, *args, **kwargs):
        if not self.password.startswith('pbkdf2_sha256$'):
            self.set_password(self.password)
        super().save(*args, **kwargs)

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
    class Meta:
        db_table = 'user'
        verbose_name = _('user')
        verbose_name_plural = _('users')
