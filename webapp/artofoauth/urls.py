from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', RedirectView.as_view(url='/twittereti/')),
                       url(r'', include('social.apps.django_app.urls', namespace='social')),
                       url(r'^logout/', 'artofoauth.apps.twittereti.views.logout_user'),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
                       url(r'^accounts/logout/$', 'django.contrib.auth.views.logout'),
                       url(r'^twittereti/', include("artofoauth.apps.twittereti.urls")),
                       ) + static(settings.STATIC_URL)