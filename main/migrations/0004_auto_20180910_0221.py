# Generated by Django 2.1.1 on 2018-09-10 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20180910_0058'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='prereqs',
        ),
        migrations.AddField(
            model_name='course',
            name='prereqs',
            field=models.ManyToManyField(blank=True, null=True, to='main.Course'),
        ),
    ]