# Generated by Django 2.1.1 on 2018-09-10 00:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('credit_hours', models.IntegerField()),
                ('prereqs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Course')),
            ],
        ),
    ]
