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
    # From Workexperience model: work_experiences
    # From Education model: educations
    # From Language model: languages
    # From Course model: courses
    # From VolunteerWork: volunteer_works

    def __unicode__(self):
        return str(self.__dict__)

class WorkExperience(DateTimeModel):
    cvs = models.ForeignKey(CV, related_name='work_experiences')

    from_date = models.DateField()
    to_date = models.DateField()
    role = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    highlights = models.CharField(max_length=100, null=True)

class Education(DateTimeModel):
    cvs = models.ForeignKey(CV, related_name='educations')
    from_date = models.DateField()
    to_date = models.DateField()
    degree = models.CharField(max_length=150)
    school = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)

class Language(DateTimeModel):
    cvs = models.ForeignKey(CV, related_name='languages')
    language = models.CharField(max_length=100)
    level = models.CharField(max_length=100)

class Course(DateTimeModel):
    cvs = models.ForeignKey(CV, related_name='courses')
    description = models.CharField(max_length=1000)

class VolunteerWork(DateTimeModel):
    cvs = models.ForeignKey(CV, related_name='volunteer_works')
    from_date = models.DateField()
    to_date = models.DateField()
    role = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
