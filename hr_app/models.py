from django.db import models

class Tasks(models.Model):
    class Status(models.TextChoices):
        DRAW = ('dra', 'черновик')
        ACTIVE=('act', 'опубликовано')
    name = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    autor = models.CharField(max_length=100)
    status = models.CharField(max_length=3, choices=Status.choices, default=Status.DRAW)


    def __str__(self):
        return self.name


# Create your models here.
