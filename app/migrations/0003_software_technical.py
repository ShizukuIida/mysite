# Generated by Django 2.2.25 on 2021-12-24 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_education_experience'),
    ]

    operations = [
        migrations.CreateModel(
            name='Software',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='ソフトウェア')),
                ('level', models.CharField(max_length=100, verbose_name='レベル')),
                ('percentage', models.IntegerField(verbose_name='パーセンテージ')),
            ],
        ),
        migrations.CreateModel(
            name='Technical',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='テクニカル')),
                ('level', models.CharField(max_length=100, verbose_name='レベル')),
                ('percentage', models.IntegerField(verbose_name='パーセンテージ')),
            ],
        ),
    ]