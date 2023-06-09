# Generated by Django 4.1.7 on 2023-02-28 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0029_rename_valuee_review_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='body',
            field=models.TextField(blank=True, default='Body', null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='demo_link',
            field=models.CharField(blank=True, default='Demo Link', max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='documents_link',
            field=models.TextField(blank=True, default='Documents Link', null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='meeting_link',
            field=models.CharField(blank=True, default='Meeting Link', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='source_link',
            field=models.CharField(blank=True, default='Source Link', max_length=200, null=True),
        ),
    ]
