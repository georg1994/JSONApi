from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.ForeignKey(User, related_name='+')
    user_type = models.BooleanField(default=False)
