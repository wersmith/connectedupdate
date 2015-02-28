from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from userprofile.serializers import UserSerializer, GroupSerializer, AppliancePreferenceSerializer, ApplianceSupplierInfoSerializer, HomeInfoSerializer
from userprofile.models import AppliancePreferences, ApplianceInfo, HomeInfo

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer

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



