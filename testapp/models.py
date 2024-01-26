from django.db import models

# Create your models here.
class TestModel(models.Model):
    query1 = models.CharField(default = "", max_length = 50)
    query2 = models.IntegerField(default = 0)