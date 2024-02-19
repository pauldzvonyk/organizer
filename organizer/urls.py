from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('task.urls')),

                  # Order is important, django.contrib.auth.urls first to handle login, logout and
                  # registration page urls for us
                  path('members/', include('django.contrib.auth.urls')),
                  path('members/', include('members.urls')),
                  # Handles default django path for password change
                  path('<int:user_id>/', include('members.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
