from django.db import models

class Post (models.Model):
    name = models.CharField(max_length=50)
    summary = models.TextField()
    averageRating = models.DecimalField()


    def __str__(self):
        return self.title