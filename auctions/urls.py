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
    path("auction/<int:auction_id>", views.auction, name="auction"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("related_auctions", views.related_auctions, name="related_auctions"),
    path("add_to_watchlist/<int:auction_id>", views.add_to_watchlist, name="add_to_watchlist"),
    path("remove_from_watchlist/<int:auction_id>", views.remove_from_watchlist, name="remove_from_watchlist"),
    path("close_auction/<int:auction_id>", views.close_auction, name="close_auction"),
]
