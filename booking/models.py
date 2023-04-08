from django.db import models
from datetime import datetime
import datetime as dt


HOUR_CHOICES = [(dt.time(hour=x), '{:02d}:00'.format(x)) for x in range(8, 19)]

SERVER_CHOICES = (
    ("one", "One"),
    ("two", "Two"),
    ("three", "Three"),
    ("four", "Four"),
    ("five", "Five"),
)


class slot(models.Model):
    customer = models.CharField(max_length=50, null=False, blank=False, default="your name")
    server = models.CharField(max_length=50, choices=SERVER_CHOICES)
    date = models.DateField(auto_now=False, auto_now_add=False, default=datetime.now)
    time = models.TimeField(auto_now=False, auto_now_add=False, choices=HOUR_CHOICES)

    def __str__(self):
        return self.customer