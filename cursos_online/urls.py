# cursos_online/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cursos.urls')),  # Esto incluirá las URLs de la app cursos
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)