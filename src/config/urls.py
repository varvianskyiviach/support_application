from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("exchange-rates/", include("exchange_rates.urls")),
    path("", include("users.urls")),
    path("", include("core.urls")),
    path("auth/", include("authentication.urls")),
]
