from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import handler404, handler400, handler403, handler500


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('projects.urls')),
    path('users/', include('users.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = 'users.views.error_404'
handler400 = 'users.views.error_404'
handler403 = 'users.views.error_404'
handler500 = 'users.views.error_500'