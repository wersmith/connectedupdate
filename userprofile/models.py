from django.db import models
from django.contrib.auth.models import User

class UserProfileData(models.Model):
    userID = models.OneToOneField(User)
    dob = models.DateField()
    dateJoined = models.DateField(auto_now_add=True)
    #displayname = models.CharField(max_length=50)

    def __str__(self):
        return str(self.userID.username)

class ApplianceInfo(models.Model):
    applianceSupplierID = models.AutoField(primary_key=True)
    applianceNameSupplier = models.CharField(max_length=50)
    applianceDescription = models.TextField(max_length=300)
    applianceHeight = models.IntegerField()
    applianceWidth = models.IntegerField()
    applianceDepth = models.IntegerField()
    
    def __str__(self):
        return str(self.applianceName)

class HomeInfo(models.Model):
    homeID = models.AutoField(primary_key=True)
    homeSquareFeet = models.IntegerField()
    homeStreetAddress = models.CharField(max_length=50)
    homeCity = models.CharField(max_length=50)
    homeZIP = models.IntegerField(max_length=5)
    homeState = models.CharField(max_length=2)
    #homeAPI_Url = models.CharField(max_length=75)

    def __str__(self):
        return str(self.homeStreetAddress)

class RoomInfo(models.Model):
    roomID = models.AutoField(primary_key=True)
    roomName = models.CharField(max_length=50)
    homeID = models.ForeignKey(HomeInfo)

    def __str__(self):
        return str(self.roomName)


class AppliancePreferences(models.Model):
    inputID = models.AutoField(primary_key=True)
    homeID = models.ForeignKey(HomeInfo)
    roomID = models.ForeignKey(RoomInfo)
    #applianceSupplierID = models.ForeignKey(ApplianceInfo)
    userID = models.ForeignKey(UserProfileData)
    applianceName = models.CharField(max_length=50)
    timeLapseAlarm = models.IntegerField()

    
    def __str__(self):
        return str(self.applianceName)


class CurrentAppliances(models.Model):
    #This is the table we will store AwareHome 
    sessionID = models.AutoField(primary_key=True)
    applianceName = models.ForeignKey(AppliancePreferences)
    applianceStartTime = models.TimeField(null=True)  #time the appliance turned on
    applianceEndTime = models.TimeField(null=True, blank=True)  #if null the appliance is still on

    def __str__(self):
        return str(self.applianceName)


