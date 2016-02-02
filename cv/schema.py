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


class Query(graphene.ObjectType):
    all_cvs = relay.ConnectionField(CV)
    cv = relay.NodeField(CV)
    viewer = graphene.Field('self')

    @resolve_only_args
    def resolve_all_cvs(self, **kwargs):
        return models.CV.objects.all()

    def resolve_viewer(self, *args, **kwargs):
        return self


schema.query = Query
