# Generated by Django 4.1.4 on 2023-01-04 00:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_project_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='owner',
        ),
        migrations.AddField(
            model_name='project',
            name='is_completed',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='mentor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.profile'),
        ),
        migrations.AddField(
            model_name='project',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='student', to='users.profile'),
        ),
        migrations.AddField(
            model_name='review',
            name='body',
            field=models.TextField(blank=True, null=True),
        ),
    ]
