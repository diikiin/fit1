from django.db import models
from wheel.metadata import _


# class Class(models.Model):



class Schedule(models.Model):
    class WeakDays(models.IntegerChoices):
        SUNDAY = 1, _('Sunday')
        MONDAY = 2, _('Monday')
        TUESDAY = 3, _('Tuesday')
        WEDNESDAY = 4, _('Wednesday')
        THURSDAY = 5, _('Thursday')
        FRIDAY = 6, _('Friday')
        SATURDAY = 7, _('Saturday')

    name = models.CharField(max_length=100)
    description = models.TextField()
    work_days = models.SmallIntegerField(choices=WeakDays.choices)


class RecordTime(models.Model):
    date = models.DateField()
    time = models.CharField(max_length=20)
    hasEmptySlots = models.BooleanField(default=False)
    maximumSlots = models.IntegerField()
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)


class Studio(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField()
    address = models.CharField(max_length=100)
    rating = models.FloatField()
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
