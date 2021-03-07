from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('',include('IW_App.urls')),
    path('login/', include('login.urls', namespace='IW_login')),
    path('login/', include("django.contrib.auth.urls")),
    path('summernote/', include('django_summernote.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
