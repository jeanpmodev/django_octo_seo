import json
from django import forms
from .models import SuperSEOPage

ROBOTS_CHOICES = [
    ("index, follow", "Index & Follow (Public — Appear on Google)"),
    ("noindex, follow", "Noindex & Follow (Hide Page, Follow Links)"),
    ("index, nofollow", "Index & Nofollow (Show Page, Ignore Links)"),
    ("noindex, nofollow", "Noindex & Nofollow (Private / Staging)"),
    ("noindex, nofollow, noarchive", "Strict Block (Noindex, Nofollow, Noarchive)"),
]

OG_TYPE_CHOICES = [
    ("website", "Website (Default)"),
    ("article", "Article / Blog Post"),
    ("product", "Product"),
    ("profile", "Profile"),
]

SCHEMA_TYPE_CHOICES = [
    ("SoftwareApplication", "SoftwareApplication"),
    ("WebSite", "WebSite"),
    ("WebPage", "WebPage"),
    ("BlogPosting", "BlogPosting"),
    ("Article", "Article"),
    ("Organization", "Organization"),
    ("Product", "Product"),
]


class SuperSEOPageAdminForm(forms.ModelForm):
    robots_directives = forms.ChoiceField(
        choices=ROBOTS_CHOICES,
        initial="index, follow",
        label="Search Engine Visibility (robots)",
        help_text="Controls whether Google and other search engines index this page.",
    )
    og_type = forms.ChoiceField(
        choices=OG_TYPE_CHOICES,
        initial="website",
        label="Social Content Type (og:type)",
        help_text="Standard Open Graph object type for WhatsApp, LinkedIn, and Slack.",
    )
    json_ld_schema_type = forms.ChoiceField(
        choices=SCHEMA_TYPE_CHOICES,
        initial="SoftwareApplication",
        label="Rich Results Category (Schema.org)",
        help_text="Defines how Google understands this page for Rich Snippets.",
    )

    class Meta:
        model = SuperSEOPage
        fields = "__all__"
        labels = {
            "page_name": "Internal Page Identifier (Slug / Key)",
            "language_code": "Page Language (ISO Code)",
            "title": "Google Search Title (<title>)",
            "description": "Google Search Summary (meta description)",
            "canonical_url": "Official Page URL (Canonical)",
            "keywords": "Topic Keywords (Comma-separated)",
            "thumbnail_image": "Search Thumbnail Image URL",
            "author": "Content Author / Organization",
            "og_title": "Social Share Title (og:title)",
            "og_description": "Social Share Summary (og:description)",
            "og_image": "Social Share Banner Image URL (1200x630)",
            "twitter_site": "Brand X / Twitter Handle",
            "twitter_creator": "Author X / Twitter Handle",
            "headline_structured": "Structured Data Headline",
            "x_frame_options": "Clickjacking Protection (X-Frame-Options)",
        }
        help_texts = {
            "page_name": "Unique key used to load this SEO profile in views or templates (e.g., home, about, pricing).",
            "title": "Main clickable headline on Google. Keep between 30 and 60 characters.",
            "description": "Short summary shown below the title on Google. Keep between 100 and 160 characters.",
            "canonical_url": "Full official URL including https:// (e.g., https://ticapsoriginal.com).",
            "og_title": "Optional. Automatically copies Google Search Title if left blank.",
            "og_description": "Optional. Automatically copies Google Search Summary if left blank.",
            "og_image": "Direct image URL shown when shared on WhatsApp, LinkedIn, or Slack.",
            "headline_structured": "Optional. Automatically copies Google Search Title if left blank.",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        optional_fields = (
            "og_title",
            "og_description",
            "og_image",
            "thumbnail_image",
            "headline_structured",
            "twitter_site",
            "twitter_creator",
        )
        for optional_field in optional_fields:
            if optional_field in self.fields:
                self.fields[optional_field].required = False

        if self.instance and self.instance.pk:
            for field_name, choices in (
                ("robots_directives", ROBOTS_CHOICES),
                ("og_type", OG_TYPE_CHOICES),
                ("json_ld_schema_type", SCHEMA_TYPE_CHOICES),
            ):
                val = getattr(self.instance, field_name, None)
                if val and not any(val == c for c in choices):
                    self.fields[field_name].choices = [(val, f"Custom ({val})")] + choices

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title") or ""
        description = cleaned_data.get("description") or ""
        thumbnail = cleaned_data.get("thumbnail_image") or ""
        og_image = cleaned_data.get("og_image") or ""

        if not cleaned_data.get("og_title"):
            cleaned_data["og_title"] = title
        if not cleaned_data.get("og_description"):
            cleaned_data["og_description"] = description
        if not og_image and thumbnail:
            cleaned_data["og_image"] = thumbnail
        if not thumbnail and og_image:
            cleaned_data["thumbnail_image"] = og_image
        if not cleaned_data.get("headline_structured"):
            cleaned_data["headline_structured"] = title
        if not cleaned_data.get("twitter_site"):
            cleaned_data["twitter_site"] = "@ticapsoriginal"
        if not cleaned_data.get("twitter_creator"):
            cleaned_data["twitter_creator"] = cleaned_data["twitter_site"]

        payload = {
            "@context": "https://schema.org",
            "@type": cleaned_data.get("json_ld_schema_type") or "SoftwareApplication",
            "headline": cleaned_data.get("headline_structured") or title,
            "url": cleaned_data.get("canonical_url") or "",
            "description": description,
        }

        try:
            serialized = json.dumps(payload, ensure_ascii=False)
            json.loads(serialized)
        except (TypeError, ValueError) as exc:
            raise forms.ValidationError(f"Invalid JSON-LD payload generated: {exc}")

        return cleaned_data
