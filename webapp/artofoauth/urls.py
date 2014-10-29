from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', include(apps.twittereti.urls)),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include("artofoauth.apps.twittereti.urls")),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)