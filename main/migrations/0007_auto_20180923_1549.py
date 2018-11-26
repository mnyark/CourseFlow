# Generated by Django 2.1.1 on 2018-09-23 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20180923_1548'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='node',
            name='concentration',
        ),
        migrations.AddField(
            model_name='node',
            name='concentration',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='concentration', to='main.Concentration'),
            preserve_default=False,
        ),
    ]
