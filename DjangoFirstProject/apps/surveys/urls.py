from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    # This line hsurveysas changed!
	url(r'^$', views.create),
	url(r'^/new$', views.new),
	]