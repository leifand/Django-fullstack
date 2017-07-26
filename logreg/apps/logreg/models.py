from __future__ import unicode_literals

from django.db import models

class UserManager(models.Manager):

    def validate(self, ninja_data):
        errors = []
        if len(ninja_data['fname']) == 0:
            errors.append("First Name is required.")
        if len(ninja_data['lname']) == 0:
            errors.append("Last Name is required.")
        if len(ninja_data['email']) == 0:
            errors.append("Email is required.")
        if len(ninja_data['pword']) == 0:
            errors.append("Password is required.")
        if ninja_data['pword'] != ninja_data['cword']:
            errors.append("Password confirmation must match password.")
        return errors

class User(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    pword = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    objects = UserManager()
