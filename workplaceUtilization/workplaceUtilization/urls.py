"""workplaceUtilization URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from django.views.generic import TemplateView
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

from clients import api
from space import api as apiSpace

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/clients/$', api.ClientList.as_view()),
    url(r'^api/(?P<client>\w+)/projects/$', api.ProjectList.as_view()),
    url(r'^api/(?P<client>\w+)/(?P<project>\w+)/buildings/$', api.BuildingList.as_view()),
    url(r'^api/(?P<client>\w+)/(?P<project>\w+)/(?P<building>\w+)/studies$', apiSpace.StudyList.as_view()),
    url(r'^api/(?P<client>\w+)/(?P<project>\w+)/(?P<building>\w+)/spaces$', apiSpace.SpaceList.as_view()),
    url(r'^api/(?P<client>\w+)/(?P<project>\w+)/(?P<building>\w+)/(?P<study>\w+)/days$', apiSpace.DayRecordList.as_view()),
    url(r'^api/(?P<client>\w+)/(?P<project>\w+)/(?P<building>\w+)/(?P<study>\w+)/spaces$', apiSpace.SpaceRecordList.as_view()),
    url(r'^api/(?P<client>\w+)/(?P<project>\w+)/(?P<building>\w+)/(?P<study>\w+)/spacesWrite$', apiSpace.SpaceRecordListVIEW.as_view()),
]
