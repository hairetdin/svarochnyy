from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^project/', include('project.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'views.home', name='home'),
    url(r'^search/$','views.search'),
    url(r'^contact/', 'views.contact'),
    url(r'^about/', 'views.about'),
    url(r'^catalog/', include('catalog.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^tinymce/filebrowser/',include('filebrowser.urls')),
    url(r'^uploadify/', include('uploadify.urls')),
)
