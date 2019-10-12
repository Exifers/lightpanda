from django.contrib.auth.models import User
from django.db import models


class Todo(models.Model):
    text = models.TextField()
    done = models.BooleanField(default=False)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
