from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
	url(r'^$', views.index),
	url(r'^regis$', views.regis),
	url(r'^login$', views.login),
	url(r'^books$', views.books),
	url(r'^add$', views.add),
	]