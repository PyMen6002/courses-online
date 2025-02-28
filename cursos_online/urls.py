# cursos_online/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cursos.urls')),  # Esto incluirá las URLs de la app cursos
]
