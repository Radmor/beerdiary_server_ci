from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

from rest_framework import routers


import pubs.api
import events.api

router = routers.DefaultRouter()

router.register(
    'pubs', pubs.api.PubViewSet, 'pubs',
)
router.register(
    'events', events.api.EventViewSet, 'events',
)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        url(r'^rosetta/', include('rosetta.urls')),
    ]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
