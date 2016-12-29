from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from photo import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^photo/(?P<photo_id>\d+)$',views.single_photo, name='view_single_photo'),
    url(r'^photo/upload/$',views.new_photo, name='new_photo'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
