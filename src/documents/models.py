from django.db import models
from django.db import modelsfrom django.conf import settings

# Create your models here.

User = settings.AUTH_USER_MODEL  # Use the custom user model if defined
class Document(models.Model):
    owner = models.ForeignKey(
        User
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    content = models.TextField(blank=True)  # Optional field for additional content
    file = models.FileField(upload_to='documents/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # Automatically update on save
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-uploaded_at']  # Order by most recent first
        verbose_name = 'Document'
        verbose_name_plural = 'Documents'  # Plural name for admin interface
