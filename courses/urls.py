from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
  url(r'^$', views.CourseList.as_view(), name="course_list"),
  url(r'^(?P<pk>[0-9]+)/$', views.CourseDetail.as_view(), name="course_detail"),
]