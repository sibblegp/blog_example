from django.db import models
from django.utils import timezone
# Create your models here.

class BlogPost(models.Model):
    post_title = models.CharField(max_length=200)
    post_text = models.TextField()
    publish_datetime = models.DateTimeField('date published')

