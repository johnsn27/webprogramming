from django.db import models

class Journalist (models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return self.first_name

r = Journalist(first_name='John', last_name='Smith', email='john@example.com')

class Post (models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    journalist = models.ForeignKey(Journalist, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

a = Post(title="title", description="description", journalist=r)