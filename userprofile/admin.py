from django.contrib import admin
from userprofile.models import UserProfileData,AppliancePreferences, ApplianceInfo, HomeInfo, RoomInfo, CurrentAppliances

admin.site.register(UserProfileData)
admin.site.register(AppliancePreferences)
admin.site.register(ApplianceInfo)
admin.site.register(HomeInfo)
admin.site.register(RoomInfo)
admin.site.register(CurrentAppliances)