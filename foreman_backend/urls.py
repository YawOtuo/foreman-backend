from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls.static import static
from django.conf import settings

from foreman_backend import views

schema_view = get_schema_view(
    openapi.Info(
        title="Your API Title",
        default_version="v1",
        description="Your API description",
        terms_of_service="https://www.example.com/policies/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/products/", include("core.urls.products")),
    path("api/users/", include("core.urls.users")),
    path("api/carts/", include("core.urls.cart")),
    path("api/favourites/", include("core.urls.favourites")),
    path("api/categories/", include("core.urls.categories")),
    path("api/emails/", include("core.urls.email")),
    path("api/orders/", include("core.urls.order")),
    path("api/dashboard/", include("core.urls.dashboard")),
    path("", views.home),
    re_path(
        r"^swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
