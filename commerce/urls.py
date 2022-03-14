from django.urls import path

from commerce.views.category_view import CategoryCrateListView
from commerce.views.product_view import CreateListProductView, ProductDetailsView

urlpatterns = [
    path('category/', CategoryCrateListView.as_view(), name='category_crate_list'),
    path('products/', CreateListProductView.as_view(), name='product_crate_list'),
    path('product/<slug>/', ProductDetailsView.as_view(), name='product_update_delete_details'),
]
