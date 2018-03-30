from django.db import models
from django.contrib.postgres.fields import JSONField

# Create your models here.

from clients.models import Client, Project, Building

class Study(models.Model):
    building = models.ForeignKey(Building,on_delete=models.CASCADE)
    study_name = models.CharField(max_length=200, unique=True)
    PROVIDERS = (
        ('Relogix','Relogix'),
        ('CoWorkr','CoWorkr'),
        ('Moby','Moby'),
    )
    study_provider = models.CharField(max_length=200, choices=PROVIDERS)
    dynamic = models.BooleanField(default=False)

    def __str__(self):
        return self.study_name

class Space(models.Model):
    building = models.ForeignKey(Building,on_delete=models.CASCADE)
    TYPES = (
        ('Me','Work Seat'),
        ('We','Group Seat'),
        ('Other','Other'),
    )
    space_type = models.CharField(max_length=200, choices=TYPES)
    space_name =  models.CharField(max_length=200)
    space_data = JSONField()
    sensor_id = models.CharField(max_length=200, blank=True, default='')

    def __str__(self):
        return self.space_name

class dayRecord(models.Model):
    study = models.ForeignKey(Study,on_delete=models.CASCADE)
    vacancy = models.IntegerField()
    peak = models.IntegerField()
    day = models.DateField()

    def __str__(self):
        return "%s %s" % (self.study, self.day)

class spaceRecord(models.Model):
    study = models.ForeignKey(Study,on_delete=models.CASCADE)
    space = models.ForeignKey(Space,on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    occ = models.IntegerField()
    pctmoment = models.FloatField()
    pctspace = models.FloatField()
    data = JSONField(default=list)

    def __str__(self):
        return "%s %s" % (self.space, self.datetime)
