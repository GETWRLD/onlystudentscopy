# Generated by Django 4.1.5 on 2023-01-10 04:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0019_remove_project_vote_ratio_remove_project_vote_total_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='is_finished',
        ),
    ]
