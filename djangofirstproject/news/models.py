from django.db import models
from tinymce.models import HTMLField
from django.utils import timezone

class News(models.Model):
    news_title = models.CharField(max_length=200)
    news_desc = HTMLField()
 
   
