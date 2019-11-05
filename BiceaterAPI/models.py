from django.db import models

# Create your models here.


class Rest(models.Model):
    first_name = models.CharField(max_length=30, default='Jose')
    last_name = models.CharField(max_length=30, default='Martin')
