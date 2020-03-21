from django.db import models


class Experience(models.Model):
    company = models.CharField(max_length=120)
    role = models.CharField(max_length=120)
    description = models.TextField()
    start_date = models.DateField(max_length=120)
    end_date = models.DateField(max_length=120, null=True, blank=True)

    def __str__(self):
        return self.company


class Field(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=120)
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='projects', null=True, blank=True)
    detail = models.TextField(null=True, blank=True)
    github_link = models.URLField()
    preview_link = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title


class Certificate(models.Model):
    course = models.CharField(max_length=120)
    university = models.CharField(max_length=120)
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    date = models.DateField()
    link = models.URLField()

    def __str__(self):
        return self.course


class Skill(models.Model):
    name = models.CharField(max_length=120)
    icon = models.CharField(max_length=120)

    def __str__(self):
        return self.name
