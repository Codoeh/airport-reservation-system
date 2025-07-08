from django.urls import path, include

from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path("token/", obtain_auth_token),
    path("auth/", include("dj_rest_auth.urls")),
    path("auth/registration/", include("dj_rest_auth.registration.urls")),
]
