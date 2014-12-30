from django.conf.urls import patterns, include, url
from django.contrib import admin
from filebrowser.sites import site

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'archersyspeanut.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^admin/filebrowser/', include(site.urls)),

    (r'^grappelli/', include('grappelli.urls')),
)
