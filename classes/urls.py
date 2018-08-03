from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
  url(r'^$', views.ClassList.as_view(), name="class_list"),
  url(r'^(?P<pk>[0-9]+)/$', views.ClassList.as_view(), name="class_detail"),
]