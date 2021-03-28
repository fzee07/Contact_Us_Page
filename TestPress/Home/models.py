from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    phone = models.IntegerField(max_length=10)
    email = models.CharField(max_length=64)
    desc = models.TextField(max_length=122, null=True)
    date = models.DateField()


def __str__(self):
    return self.Name

