
from django.conf.urls import include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    url(r'^captcha/', include('captcha.urls')),
    url(r'^contact_form/', include('contact_form.urls')),
    url(r'^admin/', admin.site.urls),
]
