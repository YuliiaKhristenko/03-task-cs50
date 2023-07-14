from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("new", views.new, name="new"),
    path("categories", views.categories, name="categories"),
    path("my_lots", views.my_lots, name="my_lots"),
    path("category_auctions/<int:category_id>", views.category_auctions, name="category_auctions"),
]
