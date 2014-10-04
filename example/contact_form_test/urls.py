from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^captcha/', include('captcha.urls')),
    url(r'^contact_form/', include('contact_form.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

