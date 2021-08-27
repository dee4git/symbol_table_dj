from django.db import models


# Create your models here.


class Symbol(models.Model):
    index = models.IntegerField(default=None, blank=True, null=True)
    name = models.CharField(default=None, max_length=100)
    type = models.CharField(default=None, max_length=100)
    size = models.IntegerField(default=None, blank=True, null=True)
    dimension = models.IntegerField(default=None, blank=True, null=True)
