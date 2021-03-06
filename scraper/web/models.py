from django.db import models
from django.contrib.auth.models import User

class Token (models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    token=models.CharField(max_length=48)
    def __str__(self):
        return '{}_token'.format(self.user)

# Create your models here.
class Car (models.Model):
    year=models.IntegerField()
    make=models.CharField(max_length=200)
    model=models.CharField(max_length=200)
    mileage=models.IntegerField()
    def __str__(self):
        return '{} {} {} {}k mi'.format(self.year,self.make,self.model,self.mileage//1000)


class Deal (models.Model):
    price=models.IntegerField()
    zipcode=models.CharField(max_length=5)
    car = models.ForeignKey(Car, on_delete=models.CASCADE) \
    #Many-to-one relationships , every car can have one ore more price in a zipcode 
    def __str__(self):
        return '{} ${} '.format(self.car,self.price)