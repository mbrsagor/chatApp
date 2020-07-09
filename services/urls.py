from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [

    path('mobile', adpost_views, name = 'adpost_views'),
    path('television', adpost_television_views, name = 'adpost_television_views'),
    path('computing', adpost_computing_views, name = 'adpost_computing_views'),
    path('property', adpost_property_views, name = 'adpost_property_views'),
    path('study', adPost_study_views, name = 'adPost_study_views'),
    path('items/', all_service_display, name = 'all_service_display'),
    path('list/', list_of_display, name = 'list_of_display'),
    path('delete/<int:id>', list_of_delete, name = 'list_of_delete'),
    path('details_item/<int:id>', Details_product.as_view(), name = 'Details_product'),

]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
