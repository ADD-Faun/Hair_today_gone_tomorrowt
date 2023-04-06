from django.db import models


class slot(models.Model):
    customer = models.CharField(max_length=50, null=False, blank=False)
    server = models.CharField(max_length=50, null=False, blank=False)
    date = models.DateField(auto_now=False, auto_now_add=False)
    time = models.TimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.name
