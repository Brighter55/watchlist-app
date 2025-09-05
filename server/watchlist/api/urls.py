from django.urls import path
from . import views


app_name = "api"


urlpatterns = [
    path("watchlist/", views.watchlist),
    path("watchlist-add/", views.watchlist_add),
    path("", views.get_JWT_token),
]
