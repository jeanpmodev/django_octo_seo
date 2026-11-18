from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.views.generic import TemplateView
from .models import SuperSEOPage


class SEORuntimeShowcaseView(TemplateView):
    template_name = "django_octo_seo/seo_showcase.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page_slug = self.kwargs.get("page_name")
        default_banner = "https://githubusercontent.com"
        now = timezone.now()

        if page_slug:
            seo_page = get_object_or_404(SuperSEOPage, page_name=page_slug)
        else:
            seo_page, _ = SuperSEOPage.objects.get_or_create(
                page_name="ticapsoriginal_home",
                defaults={
                    "title": "Django Octo SEO — Enterprise Django SEO Engine",
                    "description": "Production-grade, high-performance SEO injection engine for scalable Django infrastructures with single-query metadata rendering.",
                    "keywords": "python, django, seo, json-ld, open-graph, schema-org, django-octo",
                    "author": "Ticapsoriginal IT Professional Networking Data",
                    "canonical_url": "https://ticapsoriginal.com",
                    "thumbnail_image": default_banner,
                    "robots_directives": "index, follow",
                    "x_frame_options": "DENY",
                    "language_code": "en",
                    "og_type": "website",
                    "og_title": "Django Octo SEO — Enterprise Django SEO Engine",
                    "og_description": "A high-performance, enterprise-ready Django SEO engine built for scalable infrastructures. Core module of the Django-Octo framework.",
                    "og_image": default_banner,
                    "twitter_site": "@ticapsoriginal",
                    "twitter_creator": "@ticapsoriginal",
                    "json_ld_schema_type": "SoftwareApplication",
                    "headline_structured": "Django Octo SEO — Enterprise Django SEO Engine",
                    "date_published": now,
                    "date_modified": now,
                },
            )

        context["seo_engine"] = seo_page
        return context
