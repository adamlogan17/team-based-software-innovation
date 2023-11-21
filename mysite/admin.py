
from main.views import custom404
from django.conf import settings
from django.urls import Resolver404, resolve
from django.utils.translation import gettext as _
from django.views.decorators.common import no_append_slash
from django.http import HttpResponsePermanentRedirect, Http404

from django.contrib.admin import AdminSite


class CustomAdminSite(AdminSite):
    @no_append_slash
    def catch_all_view(self, request, url):
        if settings.APPEND_SLASH and not url.endswith('/'):
            urlconf = getattr(request, 'urlconf', None)
            try:
                match = resolve('%s/' % request.path_info, urlconf)
            except Resolver404:
                pass
            else:
                if getattr(match.func, 'should_append_slash', True):
                    return HttpResponsePermanentRedirect('%s/' % request.path)
        # raise Http404 # uncomment this line if you want to see the old 404 page that displayed error info
        return custom404(request) # comment this line out if you want to see the old 404 page that displayed error info

# Instantiate the custom admin site
customAdminSite = CustomAdminSite(name='customadmin')
