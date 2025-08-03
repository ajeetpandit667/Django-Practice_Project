from django.db import models
from tinymce.models import HTMLField

class News(models.Model):
  title=models.CharField(max_length=100)
  news_desc=HTMLField()
  
  
# Create your models here.
