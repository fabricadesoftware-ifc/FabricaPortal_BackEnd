from django.db import models
from django.utils.translation import gettext_lazy as _
from core.uploader.models import Image
from core.authentication.models import User

class New(models.Model):    
    title = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    description = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='news')
    members = models.JSONField(blank=True, null=True)
    areas = models.JSONField(blank=True, null=True)
    courses = models.JSONField(blank=True, null=True)
    tags = models.JSONField(blank=True, null=True)
    images = models.ManyToManyField(
        Image,
        related_name="+",
        default=None,
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'New'
        verbose_name = _('New')
        verbose_name_plural = _('News')
        
        