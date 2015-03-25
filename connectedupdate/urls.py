from django.conf.urls import patterns, include, url
from django.contrib import admin
from userprofile import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users',views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'home_appliances_list', views.HomeApplianceViewSet)
router.register(r'supplier_appliances_list', views.SupplierApplianceViewSet)
router.register(r'home_information_list', views.HomeInfoViewSet)
router.register(r'room_information_list', views.RoomInfoViewSet)
router.register(r'current_appliances', views.CurrentApplianceViewSet)


#API via automatic URL routing
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'connectedupdate.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
    (r'^rest-auth/', include('rest_auth.urls')),                       

)
