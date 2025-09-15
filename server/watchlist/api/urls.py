from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView

app_name = "api"


urlpatterns = [
    path("watchlist/", views.watchlist),
    path("watchlist-add/", views.watchlist_add),
    path("watching/", views.watching),
    path("watched/", views.watched),
    path("delete-add-movie/", views.delete_add_movie),
    path("sign-up/", views.sign_up),
    path("get-tokens/", views.CustomTokenObtainPairView.as_view()),
    path("refresh-token/", TokenRefreshView.as_view()),
]
