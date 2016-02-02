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

    name = models.CharField(max_length=100)
    introduction = models.CharField(max_length=100)
    # From Workexperience model: work_experience

    def __unicode__(self):
        return self.title

class WorkExperience(DateTimeModel):
    cvs = models.ForeignKey(CV, related_name='work_experience')

    from_date = models.DateField()
    to_date = models.DateField()
    role = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    highlights = models.CharField(max_length=100)
