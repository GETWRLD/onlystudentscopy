# Generated by Django 4.1.4 on 2023-01-03 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_subjects'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='social_github',
            new_name='social_instagram',
        ),
        migrations.AddField(
            model_name='profile',
            name='classs',
            field=models.IntegerField(blank=True, max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='social_telegram',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='social_vk',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='vote_ratio',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='vote_total',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
