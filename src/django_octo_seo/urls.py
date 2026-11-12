from django.urls import path
from .views import SEORuntimeShowcaseView

app_name = "django_octo_seo"

urlpatterns = [
    path("", SEORuntimeShowcaseView.as_view(), name="showcase"),
]
