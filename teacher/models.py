from django.db import models

class Students(models.Model):
    name=models.CharField(max_length=50)
    course=models.CharField(max_length=20)
    age=models.IntegerField()
    def __str__(self):
        return self.name