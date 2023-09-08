from django.contrib.auth.models import User, Group
from rest_framework import serializers
from pick_em.models import Team, Location, Schedule, League, League_Members, Picks

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'groups']

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
        fields = ['id', 'schedule_week', 'schedule_date', 'schedule_time', 'schedule_away_team', 'schedule_home_team', 'schedule_location', 'game_complete', 'away_team_score', 'home_team_score', 'game_winner']

class scheduleDataSerializer(serializers.ModelSerializer):
    schedule_away_team = teamSerializer()
    schedule_home_team = teamSerializer()
    schedule_location = locationSerializer()
    class Meta:
        model = Schedule
        fields = ['id', 'schedule_week', 'schedule_date', 'schedule_time', 'schedule_away_team', 'schedule_home_team', 'schedule_location']

class leagueSerializer(serializers.ModelSerializer):
    class Meta:
        model = League
        fields = ['id', 'league_name', 'league_admin']

class leagueMembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = League_Members
        fields = ['id', 'league_id', 'user_id']

class leagueMembersDataSerializer(serializers.ModelSerializer):
    user_id = UserSerializer()
    league_id = leagueSerializer()
    class Meta:
        model = League_Members
        fields = ['id', 'league_id', 'user_id']

class picksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picks
        fields = ['id', 'user_id', 'league_id', 'game_id', 'pick_team_id', 'outcome', 'point_stake', 'points_awarded']

class picksDataSerializer(serializers.ModelSerializer):
    user_id = UserSerializer()
    league_id = leagueSerializer()
    game_id = scheduleDataSerializer()
    pick_team_id = teamSerializer()
    class Meta:
        model = Picks
        fields = ['id', 'user_id', 'league_id', 'game_id', 'pick_team_id', 'outcome', 'point_stake', 'points_awarded']