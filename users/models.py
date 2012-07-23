from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

class Registrant(models.Model):#Rename Registrant to something relevant to site.
	user = models.OneToOneField(User)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	email = models.EmailField(max_length=100)

	def __unicode__(self):
		return self.email

def create_registrant_user_callback(sender, instance, **kwargs):
	registrant, new = Registrant.objects.get_or_created(user=instance)
post_save.connect(create_registrant_user_callback, User)