from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import TemplateView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    url(r'^chi_siamo$', TemplateView.as_view(template_name="chi_siamo.html", get_context_data=lambda: {'sezione': 'chi_siamo'})),
    url(r'^cucina$', TemplateView.as_view(template_name="gallery.html", get_context_data=lambda: {'sezione': 'cucina'})),
)

# static media
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )

# handler500 = 'main.views.nondefault_500_error'
