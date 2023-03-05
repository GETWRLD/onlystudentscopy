from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User
from .models import Profile, Teacher

def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(user=user,
        username = user.username,
        email = user.email,
        name = user.first_name
        )

post_save.connect(createProfile, sender=User)

def updateUser(sender, instance, created, **kwargs):
  profile = instance
  user = profile.user
  if created == False:
    user.username = profile.username
    user.email = profile.email
    user.save()


def deleteUser(sender, instance, **kwargs):
  try:
    user = instance.user
    user.delete()
  except:
    pass

post_save.connect(createProfile, sender=User)

post_save.connect(updateUser, sender=Profile)

post_delete.connect(deleteUser, sender=Profile)