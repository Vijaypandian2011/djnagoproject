from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('registration_app.urls')),
    path('admin/', admin.site.urls),
    path('booking', include('booking.urls')),
    path('user', include('members.urls')),
    path('dashboard/', include('dashboard_app.urls')),


]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)