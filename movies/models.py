from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    director = models.CharField(max_length=255)
    release_year = models.IntegerField()
    synopsis = models.TextField()

    def __str__(self):
        return f"{self.title} - {self.release_year}"