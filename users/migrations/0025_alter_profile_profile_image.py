# Generated by Django 4.1.5 on 2023-02-17 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0024_applyteacherrequest_reason'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, default='images/user.jpg', null=True, upload_to='images/profiles/'),
        ),
    ]
