from django.db import models
from django.utils import timezone

# Create your models here.

class Role(models.Model):

    name_role = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name_role

class User(models.Model):

    user_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    nick_name = models.CharField(max_length=200)
    time_create = models.DateTimeField(default=timezone.now)
    time_end = models.DateTimeField()
    role_user = models.OneToOneField(Role,  blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.user_name

class Paste(models.Model):

    paste_name = models.CharField(max_length=200)
    type_content_paste = models.CharField(max_length=200)
    content_paste = models.TextField()
    time_create = models.DateTimeField(default=timezone.now)
    time_end = models.DateTimeField()
    is_private = models.BooleanField(default=0)
    short_link = models.TextField()
    user_own = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.paste_name
