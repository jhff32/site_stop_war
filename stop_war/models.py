from django.db import models


class Visit(models.Model):
    user_agent = models.CharField(max_length=100)
    ip = models.CharField(max_length=50)
    country = models.CharField(max_length=50, default="Not determined")
    city = models.CharField(max_length=100,default="Not determined")
