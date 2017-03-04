from django.views.generic import TemplateView
from django.views.generic import CreateView

from .models import Pub

class PubCreateView(CreateView):
    model = Pub