from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
	url(r'^users$', views.index),
	url(r'^users/new$', views.new),
	url(r'^users/create$', views.create),
	url(r'^users/(?P<user_id>\d+)$', views.show),
	url(r'^users/(?P<user_id>\d+)/edit$', views.edit),
	url(r'^users/(?P<user_id>\d+)/update$', views.update),
	url(r'^users/(?P<user_id>\d+)/destroy$', views.delete)
	]