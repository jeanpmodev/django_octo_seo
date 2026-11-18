from django.urls import path, re_path
from .views import SEORuntimeShowcaseView

app_name = "django_octo_seo"

urlpatterns = [
    path("", SEORuntimeShowcaseView.as_view(), name="showcase"),
    re_path(r"^(?P<page_name>[^/]+)/?$", SEORuntimeShowcaseView.as_view(), name="seo_page_detail"),
]
