# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.management import call_command
from django.db import migrations, models

def loadfixture(apps, schema_editor):
    fixtures = 'language volunteer_work course'.split(' ')
    call_command('loaddata', *fixtures)

class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0003_auto_20160202_1913'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
                ('description', models.CharField(max_length=1000)),
                ('cvs', models.ForeignKey(related_name='courses', to='cv.CV')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
                ('language', models.CharField(max_length=100)),
                ('level', models.CharField(max_length=100)),
                ('cvs', models.ForeignKey(related_name='languages', to='cv.CV')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VolunteerWork',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('role', models.CharField(max_length=200)),
                ('organization', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=1000)),
                ('cvs', models.ForeignKey(related_name='volunteer_works', to='cv.CV')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RunPython(loadfixture),
    ]
