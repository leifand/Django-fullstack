from __future__ import unicode_literals

from django.db import models

# the best user model ever!!!
class UserManager(models.Manager):
    def validate(self, form_data):
        errors = []
        if len(form_data['username']) < 8:
            errors.append('Username must be over 8 characters in length!')
        if len(form_data['username']) > 24:
            errors.append('Username cannot be greater than 24 characters in length!')
        return errors


class User(models.Model):
    user_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = UserManager()
