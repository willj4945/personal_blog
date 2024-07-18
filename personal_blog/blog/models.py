from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_lengtth=100)

# Finish creating the user model.
# Figure out best pratice for password management,
