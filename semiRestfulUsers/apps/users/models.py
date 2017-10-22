# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

class UserManager(models.Manager):
	def user_validator(self, postData):
		errors = {}
		print postData['email']
		if len(postData["email"]) < 1:
			errors['email'] = "Email cannot be blank!"
		if not EMAIL_REGEX.match(postData['email']):
			errors['email'] = "Invalid Email Address!"
			
		if len(postData['fname']) < 5 or len(postData['lname']) < 5:
			errors['name']= "first and last name must be more than 5 characters"

		return errors

# Create your models here.
class User(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add = True)

	objects = UserManager()