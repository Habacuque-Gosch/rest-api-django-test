from django.db import models




class Item(models.Model):
    name = models.CharField(default='', max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_created=True)

    def __str__(self):
        return self.name
