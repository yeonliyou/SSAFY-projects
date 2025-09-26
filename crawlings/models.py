from django.db import models

# Create your models here.
class Comment(models.Model):
    company_name = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)