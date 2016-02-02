# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.management import call_command
from django.db import migrations, models

def loadfixture(apps, schema_editor):
    fixtures = 'education'.split(' ')
    call_command('loaddata', *fixtures)

class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0002_fixtures'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('degree', models.CharField(max_length=150)),
                ('school', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=1000)),
                ('cvs', models.ForeignKey(related_name='educations', to='cv.CV')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='cvs',
            field=models.ForeignKey(related_name='work_experiences', to='cv.CV'),
        ),
        migrations.RunPython(loadfixture),
    ]
