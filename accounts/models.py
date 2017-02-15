from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
    state = models.CharField(
        max_length=70,
        default="RNBQKBNR/PPPPPPPP/eeeeeeee/eeeeeeee/eeeeeeee/eeeeeeee/pppppppp/rnbqkbnr/"
    )
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )