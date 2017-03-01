from django.conf.urls import include, url
from .views import TestView
urlpatterns = [
    url(r'^create/$', TestView.as_view(), name='test'),
]