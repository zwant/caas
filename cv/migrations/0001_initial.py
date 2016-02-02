# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CV',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100)),
                ('producer', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        )

        # migrations.CreateModel(
        #     name='Starship',
        #     fields=[
        #         ('transport_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cv.Transport')),
        #         ('hyperdrive_rating', models.CharField(max_length=40)),
        #         ('MGLT', models.CharField(max_length=40)),
        #         ('starship_class', models.CharField(max_length=40)),
        #     ],
        #     options={
        #         'abstract': False,
        #     },
        #     bases=('cv.transport',),
        # ),
        #
        # migrations.AddField(
        #     model_name='people',
        #     name='homeworld',
        #     field=models.ForeignKey(related_name='residents', to='cv.Planet'),
        # ),
        # migrations.AddField(
        #     model_name='film',
        #     name='characters',
        #     field=models.ManyToManyField(related_name='films', to='cv.People', blank=True),
        # )
    ]
