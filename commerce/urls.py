from django.urls import path

from commerce.views.category_view import CategoryCrateListView, CategoryUpdateDeleteView, ModelAPIView
from commerce.views.product_view import CreateListProductView, ProductDetailsView, AllProducts

urlpatterns = [
    path('model/', ModelAPIView.as_view(), name='model_api_view'),
    path('category/', CategoryCrateListView.as_view(), name='category_crate_list'),
    path('category/<pk>/', CategoryUpdateDeleteView.as_view(), name='category_update_delete'),
    path('products/', AllProducts.as_view(), name='all_product'),
    path('product/', CreateListProductView.as_view(), name='product_crate_list'),
    path('product/<slug>/', ProductDetailsView.as_view(), name='product_update_delete_details'),
]
