"""
Definition of urls for learning_log.
"""

from django.conf.urls import include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    #url(r'^$', learning_log.views.home, name='home'),
    #url(r'^learning_log/', include('learning_log.learning_log.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/',admin.site.urls),
    url(r'',include(('learning_logs.urls','learning_logs'),namespace='learning_logs')),
    url(r'^users/',include(('users.urls','users'),namespace='users')),
]
