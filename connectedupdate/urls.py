from django.conf.urls import patterns, include, url
from django.contrib import admin
from userprofile import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users',views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'appliances', views.ApplianceViewSet)


#API via automatic URL routing
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'connectedupdate.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include(router.urls)),
    url(r'^api-auth', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),                       
)
