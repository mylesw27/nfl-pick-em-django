"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from pick_em import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'teams', views.teamViewSet)
router.register(r'locations', views.locationViewSet)
router.register(r'schedules', views.scheduleViewSet, basename="schedules")
router.register(r'scheduledata', views.scheduleDataViewSet)
router.register(r'leagues', views.leagueViewSet, basename="leagues")
router.register(r'leaguemembers', views.leagueMembersViewSet)
router.register(r'leaguemembersdata', views.leagueMembersDataViewSet)
router.register(r'picks', views.picksViewSet, basename="picks")
router.register(r'createpicks', views.createPicksViewSet)
router.register(r'picksdata', views.picksDataViewSet, basename="picksdata")

urlpatterns = [
    path('', views.home, name='home'),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
