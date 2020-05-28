from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import RedirectView
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('photos/', include('photos.urls')),

    path('', RedirectView.as_view(url='/photos/')),

    path('favicon.ico', RedirectView.as_view(url=settings.STATIC_URL+"favicon.ico")),

    # media  | comment out when debug is true
    # re_path('^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),

    # static  | comment out when debug is true
    # re_path('^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
