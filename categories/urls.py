from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from categories import views

urlpatterns = [
  url(r'^$', views.CategoryList.as_view(), name="category_list"),
  url(r'^(?P<pk>[0-9]+)/$', views.CategoryDetail.as_view(), name="category_detail"),
]