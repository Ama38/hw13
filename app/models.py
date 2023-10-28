from django.db import models

# Create your models here.


class Genre(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title


class Singer(models.Model):
    name = models.CharField(max_length=150)
    text = models.TextField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.genre}"

