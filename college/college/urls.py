from django.contrib import admin
from django.urls import include, path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', include("students.urls")),
    path('groups/', include("groups.urls")),
    path('manager/', include("manager.urls")),
    path("", views.main_page),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)