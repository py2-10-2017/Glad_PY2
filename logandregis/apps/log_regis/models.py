# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import bcrypt
from django.db import models
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

# Create your models here.
class RegisLogManager(models.Manager):
	def regis_validator(self, postData):
		errors = {}

		if not EMAIL_REGEX.match(postData['email']):
			errors['email'] = "Invalid Email Address!"

		isEmailExist = User.objects.filter(email=postData["email"])

		if isEmailExist:
			errors['email'] = "email already exists"

		if len(postData['pwd']) < 8:
			errors['pwd'] = "Password is too short"

		if postData['pwd'] != postData['pwd2']:
			errors['pwd'] = "Password are not matched"

		if len(postData['fname']) < 2 or len(postData['lname']) < 2:
			errors['name']= "first and last name must be more than 5 characters"

		return errors

	def login_validator(self, postData):
		errors = {}

		isEmailExist = User.objects.get(email=postData["email"])

		if not isEmailExist: 
			errors['email'] = "email not registered"

		if not bcrypt.checkpw(postData["pwd"].encode(), User.objects.get(email=isEmailExist.email).password.encode()):
			errors['pwd'] = "wrong password"

		return errors

# Create your models here.
class User(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add = True)

	objects = RegisLogManager()