from django.contrib.auth.models import User, Group
from rest_framework import serializers
from userprofile.models import AppliancePreferences, ApplianceInfo, HomeInfo
from userprofile.models import RoomInfo

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name','last_name','url', 'username', 'email', 'groups')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('url','name')

class AppliancePreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppliancePreferences
        depth = 2


class ApplianceSupplierInfoSerializer(serializers.ModelSerializer):
	class Meta:
		model = ApplianceInfo

class HomeInfoSerializer(serializers.ModelSerializer):
	class Meta:
		model = HomeInfo
		depth = 2	

class RoomInfoSerializer(serializers.ModelSerializer):
	class Meta:
		model = RoomInfo

