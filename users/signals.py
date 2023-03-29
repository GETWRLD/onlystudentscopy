from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User
from .models import Profile, Teacher
from django.core.mail import send_mail
from django.conf import settings

def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(user=user,
        username = user.username,
        email = user.email
        )

        send_mail(
        'Добро пожаловать в OnlyStudents',
        """Вы зарегистрировались на платформе OnlyStudents.\n 
        Сейчас вы ученик, который может только просить помощи.\n 
        Зарегистрируйтесь ментором прямо сейчас и помогайте другим!\n
        (Форма для получения роли ментора находится наверху главной страницы)\n
        Для завершения регистрации заполните форму профиля на самой платформе, зайдя в настройки аккаунта.\n
        Для смены фото профиля просим прислать свое фото нам, ответив на это письмо.\n
        (Фотография будет выставлена после ручной проверки)\n
        Хорошего пользования, команда OnlyStudents""",
        settings.EMAIL_HOST_USER,
        [profile.email],
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