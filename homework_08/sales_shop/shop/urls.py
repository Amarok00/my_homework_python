from django.urls import path
from .views import (
    ShopIndexView,
    CategoriesWithProductsTree,
    ProductsView,
    OrdersListView,
    CategoriesListView,
    CategoryCreateView,
    CategoryDetailView,
    CategoryUpdateView,
    CategoryDeleteView,
    ProductDetailView,
    get_task_info,
)

app_name = "shop"

urlpatterns = [
    path("", ShopIndexView.as_view(), name="index"),
    path("products/", ProductsView.as_view(), name="products"),
    path("products/<int:pk>", ProductDetailView.as_view(), name="product"),
    path("categories/", CategoriesListView.as_view(), name="categories"),
    path("categories/create/", CategoryCreateView.as_view(), name="create-category"),
    path("categories/<int:pk>/update/", CategoryUpdateView.as_view(), name="update-category"),
    path("categories/<int:pk>/confirm-delete/", CategoryDeleteView.as_view(), name="confirm-delete-category"),
    path("categories/<int:pk>/", CategoryDetailView.as_view(), name="category"),
    path("orders/", OrdersListView.as_view(), name="orders"),
    path("orders/task/<task_id>/", get_task_info, name="get-order-task"),
    path(
        "categories-as-tree/",
        CategoriesWithProductsTree.as_view(),
        name="categories_with_products_tree",
    ),
]
