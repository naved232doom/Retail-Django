from django.contrib import admin
from django.urls import path, include
from core.views import index, contact
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("contact/", contact, name="contact"),
    path("items/", include("items.urls")),
    path("dashboard/", include("dashboard.urls")),
    path("inbox/", include("conversation.urls")),
    path("admin/", admin.site.urls),
    path("", include("core.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
