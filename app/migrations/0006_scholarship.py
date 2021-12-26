# Generated by Django 2.2.25 on 2021-12-26 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_publications'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScholarShip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='奨学金名')),
                ('period', models.CharField(max_length=100, verbose_name='期間')),
            ],
        ),
    ]