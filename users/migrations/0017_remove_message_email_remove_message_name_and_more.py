# Generated by Django 4.1.4 on 2023-01-08 01:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_alter_message_options_alter_message_messageroom'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='email',
        ),
        migrations.RemoveField(
            model_name='message',
            name='name',
        ),
        migrations.RemoveField(
            model_name='message',
            name='subject',
        ),
    ]
