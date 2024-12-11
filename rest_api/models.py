from django.db import models




class Item(models.Model):
    name = models.CharField(default='', max_length=200, null=True, blank=True)
    password = models.CharField(default='', max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name
