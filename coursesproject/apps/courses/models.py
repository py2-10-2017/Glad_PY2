# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class CourseManager(models.Manager):
	def course_validator(self, postData):
		errors = {}

		if len(postData["name"]) < 5:
			errors['email'] = "Your name is too short!"

		if len(postData['desc']) < 15:
			errors['name']= "Your description is too short!"

		return errors

# Create your models here.
class Course(models.Model):
	name = models.CharField(max_length=255)
	desc = models.CharField(max_length=1000)
	created_at = models.DateTimeField(auto_now_add = True)

	objects = CourseManager()