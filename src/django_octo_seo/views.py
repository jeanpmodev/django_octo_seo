from django.views.generic import DetailView
from .models import SuperSEOPage

class SEORuntimeShowcaseView(DetailView):
    """
    High-performance detail view controller parsing SEO metric indices.
    """
    model = SuperSEOPage
    template_name = "seo_showcase.html"
    context_object_name = "seo_engine"

    def get_object(self, queryset=None):
        # Automatically fall back or select the active Ticapsoriginal instance
        obj, created = SuperSEOPage.objects.get_or_create(
            page_name="ticapsoriginal_home",
            defaults={
                "title": "Ticapsoriginal - Professional IT Networking",
                "description": "Ticapsoriginal it professional networking data free url checkers, sitemaps to txt...",
                "keywords": "free, sitemaps, to, txt, TLS, security, checker, markdown, pdf, xml",
                "canonical_url": "https://ticapsoriginal.com",
                "headline_structured": "Ticapsoriginal it professional networking data",
                "date_published": "2024-09-05T08:00:00+03:00",
                "date_modified": "2024-09-05T08:00:00+03:00",
                "og_title": "Ticapsoriginal - Professional IT Networking",
                "og_description": "free url checkers, sitemaps to txt, sitemaps txt to xml, tsl security...",
            }
        )
        return obj
