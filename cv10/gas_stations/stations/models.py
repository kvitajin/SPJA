from django.db import models
from datetime import datetime

# Create your models here.
class Station(models.Model):
    name = models.CharField(max_length=30)
    created = models.DateTimeField(default=datetime.now)
    cars_capacity = models.IntegerField()
    company = models.ForeignKey('Company', on_delete=models.CASCADE)

    def __str__(self):
        return "{}{}({})".format(self.company.name, self.name, self.cars_capacity)


class Company(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

