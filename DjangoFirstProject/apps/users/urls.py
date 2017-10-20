from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    # This line has changed!
	url(r'^register$', views.register),
	url(r'^login$', views.login),
	url(r'^users/new$', views.register),
	url(r'^users$', views.users),
	]
