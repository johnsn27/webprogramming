from django.db import models

class Post (models.Model):
    name = models.CharField(max_length=50)
    summary = models.TextField()
    averageRating = models.DecimalField(decimal_places=1, max_digits=3)


    def __str__(self):
        return self.name