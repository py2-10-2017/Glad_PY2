from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
	url(r'^$', views.index),
	url(r'^courses/add$', views.add),
	url(r'^courses/destroy/(?P<c_id>\d+)$', views.confirm),
	url(r'^courses/delete/(?P<c_id>\d+)$', views.delete),
	]