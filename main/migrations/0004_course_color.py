# Generated by Django 2.1.1 on 2018-09-23 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_course_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='color',
            field=models.CharField(default='#f14592', max_length=100),
            preserve_default=False,
        ),
    ]
