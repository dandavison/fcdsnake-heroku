from django.contrib.auth.models import User
from django.db import models


class Score(models.Model):
    user = models.ForeignKey(User)
    score = models.IntegerField()
    date = models.DateTimeField()
