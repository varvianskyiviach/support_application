from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
<<<<<<< HEAD
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
=======
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
>>>>>>> 9384e17 (diagram & openapi is instaled)
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Support API",
        default_version="v1",
        description="This is education OpenAPI",
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns: list = [
    path("admin/", admin.site.urls),
    path("exchange-rates/", include("exchange_rates.urls")),
    path("users/", include("users.urls")),
    path("", include("core.urls")),
    path("auth/", include("authentication.urls")),
<<<<<<< HEAD
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
=======
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name='schema-swagger-ui')
>>>>>>> 9384e17 (diagram & openapi is instaled)
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
