from django.contrib.auth.models import User, Group
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from pick_em.serializers import UserSerializer, GroupSerializer, teamSerializer, locationSerializer, scheduleSerializer, scheduleDataSerializer, leagueSerializer, leagueMembersSerializer, picksSerializer, picksDataSerializer
from pick_em.models import Team, Location, Schedule, League, League_Members, Picks

def home(request):
    return render(request, 'index.html')

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class teamViewSet(viewsets.ModelViewSet):
    serializer_class = teamSerializer
    queryset = Team.objects.all()

class locationViewSet(viewsets.ModelViewSet):
    serializer_class = locationSerializer
    queryset = Location.objects.all()

class scheduleViewSet(viewsets.ModelViewSet):
    serializer_class = scheduleSerializer
    queryset = Schedule.objects.all()

class scheduleDataViewSet(viewsets.ModelViewSet):
    serializer_class = scheduleDataSerializer
    queryset = Schedule.objects.all()

    def get_queryset(self):
        queryset = Schedule.objects.all()
        week = self.request.query_params.get('week', None)
        print(week)
        if week is not None:
            queryset = queryset.filter(schedule_week=week)
        return queryset
    
class leagueViewSet(viewsets.ModelViewSet):
    serializer_class = leagueSerializer
    queryset = League.objects.all()

class leagueMembersViewSet(viewsets.ModelViewSet):
    serializer_class = leagueMembersSerializer
    queryset = League_Members.objects.all()

class picksViewSet(viewsets.ModelViewSet):
    serializer_class = picksSerializer
    queryset = Picks.objects.all()

class picksDataViewSet(viewsets.ModelViewSet):
    serializer_class = picksDataSerializer
    queryset = Picks.objects.all()

class createPicksViewSet(viewsets.ModelViewSet):
    serializer_class = picksSerializer
    queryset = Picks.objects.all()

    def create(self, request, *args, **kwargs):
        user = request.data.get('userId')
        league = request.data.get('league')
        picks = request.data.get('picks')
        

        found_user = User.objects.get(id=user)
        found_league = League.objects.get(id=league)

        for pick in picks:
            game = Schedule.objects.get(id=pick)
            team = Team.objects.get(id=picks[pick])
            print(f'User: {found_user}, League: {found_league}, Game: {pick}, Selection: {picks[pick]}')
            existing_pick = Picks.objects.filter(user_id=found_user, league_id=found_league, game_id=game)
            if existing_pick:
                existing_pick.update(pick_team_id=team)
            else:
                new_pick = Picks.objects.create(user_id=found_user, league_id=found_league, game_id=game, pick_team_id= team)
                new_pick.save()
        return Response({'message': picks}, status=200)