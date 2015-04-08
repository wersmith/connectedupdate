from django.contrib.auth.models import User, Group
from rest_framework import serializers
from userprofile.models import AppliancePreferences, ApplianceInfo, HomeInfo
from userprofile.models import RoomInfo, UserProfileData, CurrentAppliances

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name','last_name','url', 'username', 'email', 'groups')
        paginate_by = None


class UserProfileDataSerializer(serializers.ModelSerializer):
	userID = UserSerializer(many=False)

	class Meta:
		model = UserProfileData
		fields = ('userID', 'dob', 'dateJoined')
		paginate_by = None

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('url','name')
        paginate_by = None

class AppliancePreferenceSerializer(serializers.ModelSerializer):
    userID = UserProfileDataSerializer(many=False)

    class Meta:
        model = AppliancePreferences
        fields = ('inputID','applianceName','homeID', 'userID', 'timeLapseAlarm', 'roomID' )
        depth = 1
        paginate_by = None


class ApplianceSupplierInfoSerializer(serializers.ModelSerializer):
	class Meta:
		model = ApplianceInfo
		paginate_by = None

class HomeInfoSerializer(serializers.ModelSerializer):
	class Meta:
		model = HomeInfo
		depth = 2
		paginate_by = None	

class RoomInfoSerializer(serializers.ModelSerializer):
	class Meta:
		model = RoomInfo
		paginate_by = None

class SetCurrentApplianceSerializer(serializers.ModelSerializer):
	
	applianceName = serializers.PrimaryKeyRelatedField(queryset=AppliancePreferences.objects.all())


	class Meta:
		model = CurrentAppliances
		fields = ( 'sessionID','applianceName', 'applianceTime', 'applianceState' )
		depth = 2
		paginate_by = None


class GetCurrentApplianceSerializer(serializers.ModelSerializer):

	class Meta:
		model = CurrentAppliances
		depth = 2
		paginate_by = None


class ApplianceTimeSerializer(serializers.ModelSerializer):

    homeID = serializers.PrimaryKeyRelatedField(queryset=HomeInfo.objects.all())

    class Meta:
        model = AppliancePreferences
        fields = ('inputID','applianceName', 'timeLapseAlarm', 'homeID')
        depth = 1
        paginate_by = None

