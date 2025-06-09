from django.db import models

# Create your models here.
class Document(models.Model):
    owner = User # Owner can be a username or email
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

from django.contrib.auth.models import User
# Ensure User model is imported after Document class to avoid circular import issues