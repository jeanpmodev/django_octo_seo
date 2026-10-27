from django.db import models

class OctoSEOMetadataMixin(models.Model):
    """
    Abstract architecture mixin for enterprise-grade SEO injection.
    Garante database-to-head tag integrity across modern CDNs.
    """
    title = models.CharField(
        max_length=60, 
        help_text="Metric ID 02: SERP Optimized Document Title."
    )
    description = models.TextField(
        max_length=160, 
        help_text="Metric ID 03: Search engine descriptive snippet."
    )
    keywords = models.CharField(
        max_length=255, 
        help_text="Metric ID 04: Comma-separated semantic keywords."
    )
    author = models.CharField(
        max_length=100, 
        default="Ticapsoriginal it professional networking data",
        help_text="Global publisher authorship identifier."
    )
    canonical_url = models.URLField(
        help_text="Metric ID 05: Permanent structural canonical locator."
    )
    thumbnail_image = models.CharField(
        max_length=255,
        default="ticapsoriginal1200x630.png",
        help_text="Metric ID 06: Core indexing micro-format thumbnail identifier."
    )
    robots_directives = models.CharField(
        max_length=100, 
        default="index, follow", 
        help_text="Metric ID 04: Unified multi-crawler directive matrix."
    )

    class Meta:
        abstract = True


class SuperSEOPage(OctoSEOMetadataMixin):
    """
    Concrete showcase model serving real platform dataset metrics.
    Maps directly to the dynamic rendering view layer.
    """
    page_name = models.CharField(max_length=100, unique=True)
    
    # Global Security / Architecture
    x_frame_options = models.CharField(
        max_length=20, 
        default="deny", 
        help_text="Metric ID 01: Clickjacking mitigation flag."
    )
    language_code = models.CharField(max_length=10, default="en")

    # Social Semantic Graphs (Open Graph)
    og_type = models.CharField(
        max_length=50, 
        default="oficial ticapsoriginal website", 
        help_text="Metric ID 07: Open Graph profile classification."
    )
    og_title = models.CharField(max_length=100)
    og_description = models.TextField(max_length=200)
    og_image = models.CharField(max_length=255, default="ticapsoriginal1200x630.png")

    # Twitter Protocol Matrix
    twitter_site = models.CharField(max_length=50, default="@ticapsoriginal")
    twitter_creator = models.CharField(max_length=50, default="@ticapsoriginal")

    # Structured Schema Datasets (JSON-LD Contexts)
    json_ld_schema_type = models.CharField(
        max_length=50, 
        default="BlogPosting", 
        help_text="Metric ID 08: Schema.org target context metadata."
    )
    headline_structured = models.CharField(max_length=150)
    date_published = models.DateTimeField()
    date_modified = models.DateTimeField()

    def __str__(self):
        return f"{self.page_name} | {self.title}"
