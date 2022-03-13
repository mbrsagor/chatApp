from django.urls import path

from commerce.views.category_view import CategoryCrateListView

urlpatterns = [
    path('category/', CategoryCrateListView.as_view(), name='category_crate_list'),
]
