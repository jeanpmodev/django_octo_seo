from django.urls import include, path

urlpatterns = [
    path("seo-demo/", include("django_octo_seo.urls")),
]
