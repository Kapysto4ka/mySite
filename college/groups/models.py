from django.db import models
class Group(models.Model):
    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    curator = models.CharField(max_length=100)
    average_score = models.DecimalField(max_digits=5, decimal_places=2)
    rating = models.IntegerField()
    def __str__(self):
        return self.name
