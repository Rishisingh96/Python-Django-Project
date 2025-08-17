from django.db import models

# Basic model for a user without cloud
# class Service(models.Model):
#     service_icon = models.ImageField(upload_to='services/')
#     service_title = models.CharField(max_length=50)
#     service_genre = models.CharField(max_length=100, blank=True)  # Action / Adventure
#     service_des = models.TextField()  # Short description
#     service_long_des = models.TextField(blank=True)  # Full detailed description

#     def __str__(self):
#         return self.service_title
    
# Using the base model to create a cloud service model cloud use 
class Service(models.Model):
    service_icon = models.ImageField(upload_to='services/')
    service_title = models.CharField(max_length=50)
    service_genre = models.CharField(max_length=100, blank=True)  # Action / Adventure
    service_des = models.TextField()  # Short description
    service_long_des = models.TextField(blank=True)  # Full detailed description

    def __str__(self):
        return self.service_title
    