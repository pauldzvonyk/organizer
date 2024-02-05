from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('task.urls')),

    # Order is important, django.contrib.auth.urls first to handle login, logout and registration page urls for us
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
]
