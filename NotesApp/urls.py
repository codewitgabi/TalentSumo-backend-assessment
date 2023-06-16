from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

# documentation generator
schema_view = get_schema_view(
	openapi.Info(
		title="TalentSumo NotesApp API",
		default_version="v1.0.1",
		description="Rest API for the TalentSumo NotesApp.",
		terms_of_service="https://www.google.com/policies/terms/",
		contact=openapi.Contact(email="codewitgabi222@gmail.com"),
		license=openapi.License(name="BSD License"),
		),
	public=True,
	permission_classes=[permissions.AllowAny]
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("notes/api/", include("notes.api.routes")),
    path("doc/", schema_view.with_ui("swagger", cache_timeout=0))
]
