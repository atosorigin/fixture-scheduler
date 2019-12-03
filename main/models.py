from django.db import models
from django.db.models import CharField
from datetime import datetime

class Tutorial(models.Model):
    tutorial_title = models.CharField(max_length=200)
    tutorial_content = models.TextField()
    tutorial_published = models.DateTimeField("date published",default=datetime.now())

    def __str__(self):
        return self.tutorial_title



class PremierTeams(models.Model):
    tutorial_title = models.CharField(max_length=30)
    tutorial_content = models.TextField()
    tutorial_published = models.DateTimeField("date published",default=datetime.now())

    def __str__(self):
        return self.tutorial_title

class Solution(models.Model):
    solution = models.TextField()
    team = models.IntegerField()
    week01 = models.IntegerField()
    week02 = models.IntegerField()
    week03 = models.IntegerField()
    week04 = models.IntegerField()
    week05 = models.IntegerField()
    week06 = models.IntegerField()
    week07 = models.IntegerField()
    week08 = models.IntegerField()
    week09 = models.IntegerField()
    week10 = models.IntegerField()
    week11 = models.IntegerField()
    week12 = models.IntegerField()
    week13 = models.IntegerField()
    week14 = models.IntegerField()
    week15 = models.IntegerField()
    week16 = models.IntegerField()
    week17 = models.IntegerField()
    week18 = models.IntegerField()
    week19 = models.IntegerField()
    week20 = models.IntegerField()
    week21 = models.IntegerField()
    week22 = models.IntegerField()
    week23 = models.IntegerField()
    week24 = models.IntegerField()
    week25 = models.IntegerField()
    week26 = models.IntegerField()
    week27 = models.IntegerField()
    week28 = models.IntegerField()
    week29 = models.IntegerField()
    week30 = models.IntegerField()
    week31 = models.IntegerField()
    week32 = models.IntegerField()
    week33 = models.IntegerField()
    week34 = models.IntegerField()
    week35 = models.IntegerField()
    week36 = models.IntegerField()
    week37 = models.IntegerField()
    week38 = models.IntegerField()
