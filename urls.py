
from settings import root_directory

from django.conf.urls.defaults import patterns, include

from django.contrib import admin
admin.autodiscover()

handler404 = 'django.views.defaults.page_not_found'
handler500 = 'django.views.defaults.server_error'

urlpatterns = patterns('',
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': root_directory + '/braindump/static'}),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^braindump/', include('braindump.urls')),
)
