from django.db import models
from django.db.models import Sum, Avg


class UserData(models.Model):
    dataId = models.IntegerField(primary_key=True, auto_created=True)
    id = models.CharField(max_length=10)
    area = models.CharField(max_length=2)
    tariff = models.CharField(max_length=2)


class Consumption(models.Model):
    dataId = models.IntegerField(primary_key=True, auto_created=True)
    datetime = models.DateTimeField()
    consumption = models.DecimalField(decimal_places=2, max_digits=7)

    @staticmethod
    def totalConsumption() -> object:
        return Consumption.objects.aggregate(total_consumption=Sum('consumption'))

    @staticmethod
    def avgConsumption() -> object:
        return Consumption.objects.aggregate(average_consumption=Avg('consumption'))

