from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'feastly_test.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^blog/', include('gs_blog.urls', namespace='gs_blog')),
    url(r'^admin/', include(admin.site.urls)),
)
