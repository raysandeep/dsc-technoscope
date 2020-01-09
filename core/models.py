from django.db import models
from .storageback import PublicMediaStorage
# Create your models here.
class uploader(models.Model):
    author = models.CharField(max_length=50,default=True)
    coress_author = models.CharField(max_length=50,)
    email = models.EmailField(max_length=253,)
    alt_email = models.EmailField(max_length=253,)
    phone  = models.BigIntegerField(default=0)
    file = models.FileField(storage=PublicMediaStorage())
