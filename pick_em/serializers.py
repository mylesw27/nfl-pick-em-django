from django.contrib.auth.models import User, Group
from rest_framework import serializers
from pick_em.models import Team, Location, Schedule

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class teamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'team_name', 'team_location', 'team_color_1', 'team_color_2', 'team_logo']

class locationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'location_city', 'location_state', 'location_state_abbr', 'stadium_name']

class scheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ['schedule_week', 'schedule_date', 'schedule_time', 'schedule_away_team', 'schedule_home_team', 'schedule_location']

class scheduleDataSerializer(serializers.ModelSerializer):
    schedule_away_team = teamSerializer()
    schedule_home_team = teamSerializer()
    schedule_location = locationSerializer()
    class Meta:
        model = Schedule
        fields = ['schedule_week', 'schedule_date', 'schedule_time', 'schedule_away_team', 'schedule_home_team', 'schedule_location']