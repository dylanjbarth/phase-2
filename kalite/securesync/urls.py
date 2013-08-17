from django.conf.urls.defaults import include, patterns, url

urlpatterns = patterns('securesync.views',
    url(r'^', include('securesync.devices.urls')),
    url(r'^', include('securesync.engine.urls')),
    url(r'^', include('securesync.users.urls')),
)
