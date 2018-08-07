from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from assignments import views

urlpatterns = [
  url(r'^$', views.AssignmentList.as_view(), name="assignment_list"),
  url(r'^(?P<pk>[0-9]+)/$', views.AssignmentDetail.as_view(), name="assignment_detail"),
]