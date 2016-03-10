from django.conf.urls import include, url

urlpatterns = [
    # captcha support urls
    url(r'^captcha/', include('captcha.urls')),

    # contact_form
    url(r'^contact_form/', include('contact_form.urls', namespace='contact_form')),
]
