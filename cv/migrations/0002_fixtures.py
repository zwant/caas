from django.db import migrations
from django.core.management import call_command


def loadfixture(apps, schema_editor):
    fixtures = 'cvs work_experience'.split(' ')
    call_command('loaddata', *fixtures)


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(loadfixture),
    ]
