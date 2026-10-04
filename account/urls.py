from django.urls import path
from . import views

app_name = "accounts"
urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("prof/", views.prof, name="prof"),
    path("profile/edit/", views.profile_edit, name="profile_edit"),
    path("logout/", views.logout_user, name="logout"),
]
