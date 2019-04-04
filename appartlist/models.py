from django.db import models

class Apt(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField
    price=models.IntegerField
    deposit=models.IntegerField

