from django.db import models
from django.contrib.auth.models import User

class UserProfileData(models.Model):
    userID = models.OneToOneField(User)
    dob = models.DateField()
    dateJoined = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.userID.username)
    

class AppliancePreferences(models.Model):
    homeID = models.IntegerField(primary_key=True)
    applianceID = models.IntegerField()
    userID = models.ForeignKey('UserProfileData')
    applianceName = models.CharField(max_length=50)
    timeLapseAlarm = models.IntegerField()
    
    def __str__(self):
        return str(self.applianceName)
    
