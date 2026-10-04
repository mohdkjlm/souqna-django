from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("profile/", views.profile, name="profile"),
    path("add/product", views.add_product, name="add_product"),
    path("my/products", views.my_products, name="my_products"),
    path("product/detail/<int:id>/", views.product_detail, name="product_detail"),
    path("edit/product<int:id>", views.edit_product, name="edit_product"),
    path("products/", views.products, name="products"),
    path(
        "category/products/<str:category>",
        views.category_products,
        name="category_products",
    ),
    path("search/", views.search, name="search"),
    path("delete/product/<int:id>", views.delete_product, name="delete_product"),
    path("my/self", views.my_self, name="my_self"),
    path("edit/profile", views.edit_profile, name="edit_profile"),
]
