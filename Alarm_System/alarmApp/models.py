from django.db import models

class Alarm(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    time = models.TimeField(null=True, blank=True)

    def __str__(self):
        return self.title
