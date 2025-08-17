from django.db import models
from cloudinary.models import CloudinaryField

# Using Cloudinary model for cloud storage
class Service(models.Model):
    service_icon = CloudinaryField('image', folder='services/')
    service_title = models.CharField(max_length=50)
    service_genre = models.CharField(max_length=100, blank=True)  # Action / Adventure
    service_des = models.TextField()  # Short description
    service_long_des = models.TextField(blank=True)  # Full detailed description

    def __str__(self):
        return self.service_title
    