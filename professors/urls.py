from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from professors import views

urlpatterns = [
  url(r'^$', views.ProfessorList.as_view(), name="professor_list"),
  url(r'^(?P<pk>[0-9]+)/$', views.ProfessorDetail.as_view(), name="professor_detail"),
]