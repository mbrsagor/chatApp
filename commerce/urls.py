from django.urls import path

from commerce.views.category_view import CategoryCrateListView, CategoryUpdateDeleteView, ModelAPIView
from commerce.views.product_view import CreateListProductView, ProductDetailsView, AllProductsView

urlpatterns = [
    path('model/', ModelAPIView.as_view(), name='model_api_view'),
    path('category/', CategoryCrateListView.as_view(), name='category_crate_list'),
    path('category/<pk>/', CategoryUpdateDeleteView.as_view(), name='category_update_delete'),
    path('products/', AllProductsView.as_view(), name='all_products'),
    path('product/', CreateListProductView.as_view(), name='product_crate_list'),
    path('product/<slug>/', ProductDetailsView.as_view(), name='product_update_delete_details'),
]
