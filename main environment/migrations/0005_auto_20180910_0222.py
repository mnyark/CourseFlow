# Generated by Django 2.1.1 on 2018-09-10 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20180910_0221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='prereqs',
            field=models.ManyToManyField(blank=True, to='main.Course'),
        ),
    ]
