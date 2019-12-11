from django.db import models
from django.db.models import CharField
from datetime import datetime

class League(models.Model):
    name = models.CharField(max_length=255)
    sport = models.CharField(max_length=255)
    leagues = models.Manager()

class Team(models.Model):
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    teams = models.Manager()

class Run(models.Model):
    date = models.DateField()                               # When was the supercomputer run executed
    name = models.CharField(max_length=255)                 # e.g. we ran with xyz rules switched off
    notes = models.TextField()                              
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    runs = models.Manager()
    
class Period(models.Model):
    name = models.CharField(max_length=255)                 # This is a reference to the week, e.g. week01, week02
    desc = models.TextField()                               # If the league period is not weekly, then this
    periods = models.Manager()                              # period references for example the month, e.g. month01, etc

class Schedule(models.Model): 
    run = models.ForeignKey(Run, on_delete=models.CASCADE)  # reference to which supercomputer run produced this schedule
    name = models.CharField(max_length=255)                 # e.g. PL12. In the past this was the solution hash key
    desc = models.TextField()                               # e.g. Premier League 2020 final solution
    schedules = models.Manager()

class Schedule_line_item(models.Model): 
    period = models.ForeignKey(Period, on_delete=models.CASCADE)
    home_team = models.ForeignKey(Team, related_name='home_team', on_delete=models.CASCADE)
    away_team = models.ForeignKey(Team, related_name='away_team', on_delete=models.CASCADE)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    schedule_line_items = models.Manager()

