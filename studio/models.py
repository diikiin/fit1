from django.db import models


class Studio(models.Model):
    name = models.CharField(max_length=100, null=False)
    type = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Schedule(models.Model):
    studio = models.OneToOneField(Studio, on_delete=models.CASCADE)

    def __str__(self):
        return f"Schedule for {self.studio.name}"


class ExerciseClass(models.Model):
    class WeakDays(models.IntegerChoices):
        SUNDAY = 1, 'Sunday'
        MONDAY = 2, 'Monday'
        TUESDAY = 3, 'Tuesday'
        WEDNESDAY = 4, 'Wednesday'
        THURSDAY = 5, 'Thursday'
        FRIDAY = 6, 'Friday'
        SATURDAY = 7, 'Saturday'

    name = models.CharField(max_length=100, null=False)
    description = models.TextField(null=True, blank=True)
    weekday = models.IntegerField(choices=WeakDays.choices)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class RecordTime(models.Model):
    date = models.DateField()
    time = models.CharField(max_length=20)
    hasEmptySlots = models.BooleanField(default=False)
    maximumSlots = models.IntegerField()
    exerciseClass = models.ForeignKey(ExerciseClass, on_delete=models.CASCADE)

    def __str__(self):
        return f"Record time for {self.exerciseClass.name} at {self.date}"


class Address(models.Model):
    region = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    studio = models.OneToOneField(Studio, on_delete=models.CASCADE)

    def __str__(self):
        return f"Address of {self.studio.name}"


class StudioRating(models.Model):
    average = models.FloatField()
    studio = models.OneToOneField(Studio, on_delete=models.CASCADE)

    def __str__(self):
        return f"Average rating for {self.studio.name}"


class Ratings(models.Model):
    rating = models.FloatField()
    reason = models.TextField(null=True, blank=True)
    studio_rating = models.ForeignKey(StudioRating, on_delete=models.CASCADE)

    def __str__(self):
        return f"Ratings of {self.studio_rating.studio.name}"
