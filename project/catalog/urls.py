from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^project/', include('project.foo.urls')),

    url(r'^proizvoditel/(?P<proizvoditel>[\w]+)/$', 'catalog.views.proizvoditel'),
    url(r'^proizvoditel/(?P<proizvoditel>[\w]+)/(?P<category>[\w]+)/$', 'catalog.views.prozvoditel_category'),
    url(r'^category/(?P<category>[\w]+)/$', 'catalog.views.category'),
    url(r'^category/(?P<category>[\w]+)/(?P<proizvoditel>[\w]+)/$', 'catalog.views.category_proizvoditel'),
    url(r'^tovar/(?P<tovar>[\w]+)/$', 'catalog.views.tovar_detail'),
)
