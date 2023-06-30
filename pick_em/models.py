from django.db import models

# Create your models here.

class Team(models.Model):
    team_name = models.CharField(max_length=50)
    team_location = models.CharField(max_length=50)
    team_color_1 = models.CharField(max_length=7)
    team_color_2 = models.CharField(max_length=7)
    team_logo = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f'{self.team_location} {self.team_name}'

class Location(models.Model):
    location_city = models.CharField(max_length=50)
    location_state = models.CharField(max_length=50)
    location_state_abbr = models.CharField(max_length=3)
    stadium_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.location_city}, {self.location_state_abbr} - {self.stadium_name}'
    
class Schedule(models.Model):
    schedule_date = models.DateField()
    schedule_time = models.TimeField()
    schedule_week = models.IntegerField()
    schedule_away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_team')
    schedule_home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_team')
    schedule_location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return f'Week {self.schedule_week} - {self.schedule_away_team.team_name} @ {self.schedule_home_team.team_name}'

class League(models.Model):
    league_name = models.CharField(max_length=50)
    league_admin = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    league_members = models.ManyToManyField('auth.User', through='League_Members', related_name='league_members')
    
    def __str__(self):
        return self.league_name

class League_Members(models.Model):
    league_id = models.ForeignKey(League, on_delete=models.CASCADE)
    user_id = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.league_id} - {self.user_id}'
    
class Picks(models.Model):
    user_id = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    league_id = models.ForeignKey(League, on_delete=models.CASCADE)
    game_id = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    pick_team_id = models.ForeignKey(Team, on_delete=models.CASCADE, blank=True, null=True)




