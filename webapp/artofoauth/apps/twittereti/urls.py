from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('artofoauth.apps.twittereti',
    # Examples:
    url(r'^$', 'views.home'),
    # url(r'^blog/', include('blog.urls')),
)
