from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    date_of_death = models.DateField(blank=True, null=True)
    bio = models.TextField(blank=True)

    @property
    def full_name(self):
        return f'{self.name} {self.lastname}'

    def __str__(self):
        return self.full_name


class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey('Author', on_delete=models.CASCADE,
                               related_name='books')
    summary = models.TextField(blank=True)
    pages = models.IntegerField()
    genres = models.ManyToManyField('Genre', related_name='books')

    def __str__(self):
        return f'{self.name} - {self.author}'
