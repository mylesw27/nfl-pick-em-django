from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from pick_em.serializers import UserSerializer, GroupSerializer, teamSerializer, locationSerializer, scheduleSerializer, scheduleDataSerializer
from pick_em.models import Team, Location, Schedule


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