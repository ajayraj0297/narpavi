# Generated by Django 3.1.1 on 2020-10-01 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0011_courses_obj'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='trend',
            field=models.CharField(choices=[('yes', 'yes'), ('no', 'no')], default='no', max_length=20),
        ),
    ]