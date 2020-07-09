from django.contrib import admin
from django.urls import path,include
from django.conf.urls import handler404, handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('userinfo.urls')),
    path('services/', include('services.urls')),
]

# handler404 = services_views.error_404
