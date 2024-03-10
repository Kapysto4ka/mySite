from django.db import models
class Student(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    group = models.CharField(max_length=100)
    age = models.IntegerField()
    score = models.IntegerField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    def __str__(self):
        return f'{self.name} {self.surname}'
