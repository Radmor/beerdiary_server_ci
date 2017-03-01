from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

import pubs.urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^pubs/', include(pubs.urls, namespace='pubs'))
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
