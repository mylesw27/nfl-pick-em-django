from django.db import models

# Create your models here.

class Team(models.Model):
    team_name = models.CharField(max_length=50)
    team_location = models.CharField(max_length=50)
    team_color_1 = models.CharField(max_length=7)
    team_color_2 = models.CharField(max_length=7)
    team_logo = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.team_name

class Location(models.Model):
    location_city = models.CharField(max_length=50)
    location_state = models.CharField(max_length=50)
    location_state_abbr = models.CharField(max_length=3)
    stadium_name = models.CharField(max_length=50)

    def __str__(self):
        return self.location_city
    
class Schedule(models.Model):
    schedule_date = models.DateField()
    schedule_time = models.TimeField()
    schedule_week = models.IntegerField()
    schedule_away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_team')
    schedule_home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_team')
    schedule_location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.schedule_date