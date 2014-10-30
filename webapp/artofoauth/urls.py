from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', RedirectView.as_view(url='/twittereti')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
                       url(r'^accounts/logout/$', 'django.contrib.auth.views.logout'),
                       url(r'^twittereti/home', include("artofoauth.apps.twittereti.urls")),
                       #url(r'^fileupload/', include("precis.apps.resumeparser.urls")),
                       #url(r'^hirepeak/', include("precis.apps.hirepeak_api.urls")),
                       #url(r'^feedback/', include("precis.apps.feedback.urls")),
                       #url('', include('social.apps.django_app.urls', namespace='social')),
                       ) + static(settings.STATIC_URL)