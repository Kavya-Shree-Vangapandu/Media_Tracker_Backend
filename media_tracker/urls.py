from django.contrib import admin
from django.urls import path, include  # Add 'include' here
from media_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('api/', include('media_app.urls')),  # Now 'include' is properly imported
]

