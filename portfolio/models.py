from django.db import models


# Create your models here.
class Skills(models.Model):
    name = models.CharField(max_length=50, blank=False)
    progress = models.IntegerField()

    def __str__(self):
        return self.name


class Education(models.Model):
    duration = models.CharField(max_length=50, blank=False)
    university = models.CharField(max_length=200, blank=False)
    program = models.CharField(max_length=100, blank=False)
    description = models.TextField()

    def __str__(self):
        return self.program


class Projects(models.Model):
    image = models.ImageField(upload_to="static/img/", blank=True)
    summary = models.TextField(null=True)
    name = models.CharField(max_length=200)
    url = models.URLField(null=True)

    def __str__(self):
        return self.name


class Blogs(models.Model):
    image = models.ImageField(upload_to="static/img/")
    description = models.TextField(null=True)
    title = models.CharField(max_length=200)
    url = models.URLField(null=True)

    def __str__(self):
        return self.title


class WorkExperiences(models.Model):
    duration = models.CharField(max_length=50, blank=False)
    company = models.CharField(max_length=200, blank=False)
    occupation = models.CharField(max_length=100, blank=False)
    description = models.TextField()

    def __str__(self):
        return self.occupation
