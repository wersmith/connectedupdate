from django.shortcuts import render
import requests, sys
from django.contrib.auth.models import User, Group
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from userprofile.serializers import UserSerializer, GroupSerializer, AppliancePreferenceSerializer, ApplianceSupplierInfoSerializer, HomeInfoSerializer
from userprofile.serializers import RoomInfoSerializer, GetCurrentApplianceSerializer, SetCurrentApplianceSerializer, ApplianceTimeSerializer
from userprofile.models import AppliancePreferences, ApplianceInfo, HomeInfo, RoomInfo, CurrentAppliances


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_fields=('username',)

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class HomeApplianceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows home appliance information to be viewed or edited.
    """
    queryset = AppliancePreferences.objects.all()
    serializer_class = AppliancePreferenceSerializer

class SupplierApplianceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows home appliance information to be viewed or edited.
    """
    queryset = ApplianceInfo.objects.all()
    serializer_class = ApplianceSupplierInfoSerializer

class HomeInfoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows home information to be viewed or edited.
    """
    queryset = HomeInfo.objects.all()
    serializer_class = HomeInfoSerializer

class RoomInfoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows home information to be viewed or edited.
    """
    queryset = RoomInfo.objects.all()
    serializer_class = RoomInfoSerializer

class SetCurrentApplianceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows current appliance information to be viewed or edited.
    """
    
    queryset = CurrentAppliances.objects.all()
    serializer_class = SetCurrentApplianceSerializer
    filter_fields=('sessionID', 'applianceName','applianceTime','applianceState', )

    # def update(self, request, *args, **kwargs):
    #     print request
    #     partial = kwargs.pop('partial', False)
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance, data=request.data, partial=partial)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_update(serializer)
    #     return Response(serializer.data)


class GetCurrentApplianceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows current appliance information to be viewed or edited.
    """
    #most recent filter
    # queryset = CurrentAppliances.objects.all()
    def get_queryset(self):
        queryset_all = CurrentAppliances.objects.all().order_by('-sessionID')
        queryset_ids = []
        found_appliances = []
        for appliance in queryset_all:
            if appliance.applianceName not in found_appliances:
                found_appliances.append(appliance.applianceName)
                queryset_ids.append(appliance.sessionID)

        return CurrentAppliances.objects.filter(sessionID__in = queryset_ids)

    serializer_class = GetCurrentApplianceSerializer
    filter_fields=('sessionID', 'applianceName','applianceTime','applianceState', )


class ApplianceTimeViewSet(viewsets.ModelViewSet):
    """
    API endpoint allows timelapse preference to be set
    """
    filter_fields=('inputID','applianceName', 'timeLapseAlarm', 'homeID', )

    queryset = AppliancePreferences.objects.all()
    serializer_class = ApplianceTimeSerializer

    def update(self, request, *args, **kwargs):
         print request.body
         partial = kwargs.pop('partial', False)
         instance = self.get_object()
         serializer = self.get_serializer(instance, data=request.data, partial=partial)
         serializer.is_valid(raise_exception=True)
         self.perform_update(serializer)
         return Response(serializer.data)





