from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import handler404, handler400, handler403, handler500
from django.views.static import serve



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('projects.urls')),
    path('users/', include('users.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += [re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }), ]

handler404 = 'users.views.error_404'
handler400 = 'users.views.error_404'
handler403 = 'users.views.error_404'
handler500 = 'users.views.error_500'