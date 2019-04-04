from django.db import models
from model_utils import Choices

class Apt(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField()
    price=models.IntegerField()
    deposit=models.IntegerField()
    photo_link = models.CharField(max_length=700)
    bedrooms=models.FloatField(default=1)
    bathrooms=models.FloatField(default=1)
    TYPE_CHOICES = Choices('Private', 'Appartment_complex')
    type=models.CharField(max_length=25, choices=TYPE_CHOICES, default=TYPE_CHOICES.Private)
    pool=models.BooleanField(default=False)
    gym=models.BooleanField(default=False)
    renters_website = models.CharField(max_length=200)
    sorce_link = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    is_visited = models.BooleanField(default=False)
    move_in_date = models.DateField()
    appointment_date=models.DateTimeField()
    comment=models.TextField()
    phone=models.CharField(max_length=50)
    date_added=models.DateTimeField(auto_now_add=True)
    LAUNDRY_CHOICES = Choices('In_unit', 'In_complex', "Hook", "None")
    laundry = models.CharField(max_length=25, choices=LAUNDRY_CHOICES, default=LAUNDRY_CHOICES.In_complex)




