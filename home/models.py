from django.db import models


class List(models.Model):
    task = models.CharField(max_length=200)

    def __str__(self):
        return self.task
