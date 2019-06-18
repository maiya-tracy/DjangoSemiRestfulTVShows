from __future__ import unicode_literals
from django.db import models
from datetime import datetime

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['form_title']) < 2:
            errors['title'] = "TV show title should be at least two characters"
        if len(postData['form_network']) < 3:
            errors['network'] = "Network should be at least 3 characters"
        if (len(postData['form_description']) < 10 and len(postData['form_description']) > 0):
            errors['description'] = "Description should be at least 10 characters"
        if len(postData['form_release_date']) == False:
            errors['release_date'] = "Release date cannot be empty"
        stripped_date = datetime.strptime(postData['form_release_date'], '%Y-%m-%d')
        if stripped_date > datetime.now():
            errors['release_date'] = "Release date cannot be in the future"
        return errors
    def title_validator(self, postData):
        errors = {}
        entered_title = postData['form_title']
        current_records_with_title = Show.objects.filter(title=entered_title)
        if len(current_records_with_title) != 0:
            errors['title'] = "Title already in the database"
        return errors

class Show(models.Model):
    title = models.CharField(max_length = 255)
    network = models.CharField(max_length = 255)
    release_date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()
    def __repr__(self):
        return f"<User object: {self.title} {self.network} {self.release_date} {self.description} ({self.id})>"
