# Generated by Django 2.1.1 on 2018-11-25 22:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_course_semester'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='prereqs',
        ),
    ]
