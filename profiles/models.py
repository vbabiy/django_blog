from django.db import models
from django.contrib.auth import models as auth_models

class User(auth_models.User):
    mugshot=models.ImageField(upload_to='mugshots/')
