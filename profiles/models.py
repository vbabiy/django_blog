from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
	mugshot=models.ImageField(upload_to='mugshots/')
	user = models.ForeignKey(User, unique=True)

	def __unicode__(self):
		return self.user.username

	def get_absolute_url(self):
		return "/profiles/%s/" % self.user.username
