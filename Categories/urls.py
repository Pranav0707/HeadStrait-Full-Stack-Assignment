from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.category_view,name="index"),
    path("update/<int:pk>",views.update_category_details,name="update_category_details"),
    path("delete_category/<int:pk>/",views.delete_category,name="delete_category"),
    path("delete_product/<int:pk>/",views.delete_product,name="delete_product"),
    path("product_detail/<int:pk>/",views.product_detail,name="product_detail"),
    path("logout/",views.Userlogout,name="logout")
]