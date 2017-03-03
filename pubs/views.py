from django.views.generic import TemplateView
from django.views.generic import CreateView

from .models import Pub

class TestView(TemplateView):
    template_name = 'pubs/test.html'

class PubCreateView(CreateView):
    model = Pub