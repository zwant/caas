from __future__ import unicode_literals

from django.db import models


class DateTimeModel(models.Model):
    """ A base model with created and edited datetime fields """

    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class CV(DateTimeModel):
    """ A CV """

    title = models.CharField(max_length=100)
    producer = models.CharField(max_length=100)

    def __unicode__(self):
        return self.title
