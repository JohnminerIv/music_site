from django.db import models


class Musician(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Band(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Musician, through='BandMembership')

    def __str__(self):
        return self.name


class BandMembership(models.Model):
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE, null=True)
    band = models.ForeignKey(Band, on_delete=models.CASCADE, null=True)
    date_joined = models.DateField()
    position = models.CharField(max_length=64)

    def __str__(self):
        return self.musician.name + ' is in ' + self.band.name


class Album(models.Model):
    band = models.ForeignKey(Band, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    publish_date = models.DateTimeField()

    def __str__(self):
        return self.name


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    num_stars = models.IntegerField()
    length = models.IntegerField()

    def __str__(self):
        return self.name
