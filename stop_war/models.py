from django.db import models


class Visit(models.Model):
    user_agent = models.CharField(max_length=100)
    ip = models.CharField(max_length=50)
