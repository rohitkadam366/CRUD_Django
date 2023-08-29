from django.db import models

# Create your models here.
class POST(models.Model):
    title = models.CharField('Title', max_length=50)
    desc=models.TextField()
