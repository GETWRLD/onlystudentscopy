# Generated by Django 4.1.5 on 2023-02-18 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0027_rename_valuee_review_value'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='value',
        ),
        migrations.AddField(
            model_name='review',
            name='valuee',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default=None, max_length=200),
        ),
    ]
