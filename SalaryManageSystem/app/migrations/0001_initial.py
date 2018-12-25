# Generated by Django 2.1.4 on 2018-12-24 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('sex', models.CharField(max_length=16)),
                ('year', models.IntegerField(max_length=16)),
                ('job', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='salasy',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('sex', models.CharField(max_length=20)),
                ('salasy', models.FloatField(max_length=20)),
                ('Bonus', models.FloatField(max_length=20)),
                ('fakuan', models.FloatField(max_length=20)),
                ('Overtime_pay', models.FloatField(max_length=20)),
            ],
        ),
    ]