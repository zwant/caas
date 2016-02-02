import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import graphene
from graphene import resolve_only_args, relay
from graphene.contrib.django import DjangoNode, DjangoConnection

import models


schema = graphene.Schema(name='cv Relay Schema')


class Connection(DjangoConnection):
    total_count = graphene.Int()

    def resolve_total_count(self, args, info):
        return len(self.get_connection_data())

class CV(DjangoNode):

    '''A single CV.'''
    class Meta:
        model = models.CV
        exclude_fields = ('created', 'edited')

class WorkExperience(DjangoNode):
    class Meta:
        model = models.WorkExperience
        exclude_fields = ('created', 'edited')

class Education(DjangoNode):
    class Meta:
        model = models.Education
        exclude_fields = ('created', 'edited')

class Language(DjangoNode):
    class Meta:
        model = models.Language
        exclude_fields = ('created', 'edited')

class Course(DjangoNode):
    class Meta:
        model = models.Course
        exclude_fields = ('created', 'edited')

class VolunteerWork(DjangoNode):
    class Meta:
        model = models.VolunteerWork
        exclude_fields = ('created', 'edited')

class Query(graphene.ObjectType):
    all_cvs = relay.ConnectionField(CV)
    cv = relay.NodeField(CV)
    work_experience = relay.NodeField(WorkExperience)
    education = relay.NodeField(Education)
    language = relay.NodeField(Language)
    course = relay.NodeField(Course)
    volunteer_work = relay.NodeField(VolunteerWork)

    viewer = graphene.Field('self')

    @resolve_only_args
    def resolve_all_cvs(self, **kwargs):
        return models.CV.objects.all()

    def resolve_viewer(self, *args, **kwargs):
        return self


schema.query = Query
