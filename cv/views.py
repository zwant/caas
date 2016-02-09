import json
import models
import forms
from importer import json_schema
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseBadRequest
from jsonschema import ValidationError
from django.views.generic import View

class CVFormView(View):
    form_class = forms.CVForm
    template_name = 'cv_form_template.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        try:
            if 'json_data' in request.POST:
                json_data = json.loads(request.POST['json_data'])
            else:
                json_data = json.loads(request.body)
            json_schema.validate_document(json_data)
            obj = models.CV(name=json_data['name'],
                      introduction=json_data['introduction'])
            obj.save()
            if 'work_experience' in json_data:
                for work_experience_json in json_data['work_experience']:
                    obj.work_experiences.create(**work_experience_json)

            if 'volounteer_work' in json_data:
                for volounteer_work_json in json_data['volounteer_work']:
                    obj.volunteer_works.create(**volounteer_work_json)

            if 'course' in json_data:
                for course_json in json_data['course']:
                    obj.courses.create(**course_json)

            if 'education' in json_data:
                for education_json in json_data['education']:
                    obj.educations.create(**education_json)

            if 'language' in json_data:
                for language_json in json_data['language']:
                    obj.languages.create(**language_json)

        except ValueError, e:
            return HttpResponseBadRequest("Invalid JSON: {}".format(e))
        except ValidationError, e:
            return HttpResponseBadRequest("Validation error: {}".format(e))
        if 'json_data' in request.POST:
            return redirect('cv')
        else:
            return HttpResponse(status=201)
