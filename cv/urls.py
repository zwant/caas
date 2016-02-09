from django.conf.urls import url
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt

import views

urlpatterns = [
    url(r'^cv/$', csrf_exempt(views.CVFormView.as_view()), name='cv'),
    url(r'^$', TemplateView.as_view(template_name="index.html")),
]
