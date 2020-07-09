from django.urls import path
# from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm
from django.conf import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [

    path('singup', singup_views, name = 'singup_views'),
    path('singin', singin_views, name = 'singin_views'),
    path('singout', singout_views, name = 'singout_views'),
    path('profile', user_profile_views , name = 'user_profile_views'),
    path('setting', profile_setting_views , name = 'profile_setting_views'),
    path('', homepage, name = 'homepage'),
    path('services', services_views, name = 'services_views'),
    path('add-team', add_teamMember_views, name = 'add_teamMember_views'),
    path('review', add_review_views, name = 'add_review_views'),
    path('dashboard', dashboard_views, name = 'dashboard_views'),
    path('price', add_pricing_views, name = 'add_pricing_views'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
