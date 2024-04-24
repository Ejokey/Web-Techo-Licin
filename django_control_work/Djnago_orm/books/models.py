from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    year = models.IntegerField()
    pages = models.IntegerField()
    sold = models.IntegerField()

    def __str__(self):
        return self.title
