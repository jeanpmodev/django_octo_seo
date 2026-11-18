import json
from django.apps import apps
from django.contrib import admin
from django.utils import timezone
from django.utils.safestring import mark_safe
from django.utils.html import escape
from .forms import SuperSEOPageAdminForm
from .models import SuperSEOPage


class OctoSEOMetadataAdminMixin:
    @admin.display(description="SEO Health")
    def seo_health_badge(self, obj):
        title_len = len(obj.title or "")
        desc_len = len(obj.description or "")
        has_canonical = bool(obj.canonical_url)
        has_og_image = bool(obj.og_image or obj.thumbnail_image)

        if 30 <= title_len <= 60 and 100 <= desc_len <= 160 and has_canonical and has_og_image:
            color, label = "#16a34a", f"Optimal ({title_len}/60 | {desc_len}/160)"
        elif title_len > 0 and desc_len > 0:
            missing = []
            if not has_canonical:
                missing.append("No Canonical")
            if not has_og_image:
                missing.append("No OG Image")
            suffix = f" · {', '.join(missing)}" if missing else ""
            color, label = "#d97706", f"Review ({title_len}/60 | {desc_len}/160{suffix})"
        else:
            color, label = "#dc2626", "Incomplete"

        return mark_safe(
            f'<span style="background:{color}; color:#fff; padding:3px 8px; '
            f'border-radius:4px; font-weight:600; font-size:11px; white-space:nowrap;">{escape(label)}</span>'
        )

    @admin.display(description="Live SERP & Social Preview")
    def live_seo_preview(self, obj):
        url_val = escape((obj.canonical_url if obj else "") or "https://ticapsoriginal.com")
        title_val = escape((obj.title if obj else "") or "Django Octo SEO — Enterprise Django SEO Engine")
        desc_val = escape(
            (obj.description if obj else "")
            or "Production-grade, high-performance SEO injection engine designed for scalable web infrastructures."
        )
        og_title_val = escape((obj.og_title if obj else "") or title_val)
        og_desc_val = escape((obj.og_description if obj else "") or desc_val)
        og_img_val = escape(
            (obj.og_image if obj else "")
            or "https://raw.githubusercontent.com/jeanpmodev/jeanpmodev/main/assets/django-octo.jpg"
        )

        html = f"""
        <div style="display:flex; flex-wrap:wrap; gap:16px; max-width:1100px;">
            <div style="flex:1; min-width:320px; max-width:520px; padding:14px; border:1px solid #dfe1e5; border-radius:8px; background:#fff; font-family:Arial, sans-serif;">
                <div style="font-size:11px; font-weight:700; color:#5f6368; margin-bottom:8px; text-transform:uppercase;">Google Search Preview</div>
                <div id="octo-serp-url" style="font-size:12px; color:#202124; margin-bottom:4px; word-break:break-all;">{url_val}</div>
                <a id="octo-serp-link" href="{url_val}" target="_blank" rel="noopener" style="text-decoration:none;">
                    <div id="octo-serp-title" style="font-size:18px; color:#1a0dab; line-height:1.3; margin-bottom:4px;">{title_val}</div>
                </a>
                <div id="octo-serp-desc" style="font-size:13px; color:#4d5156; line-height:1.4;">{desc_val}</div>
            </div>
            <div style="flex:1; min-width:300px; max-width:440px; border:1px solid #dadde1; border-radius:8px; overflow:hidden; background:#f0f2f5; font-family:Helvetica, Arial, sans-serif;">
                <div style="font-size:11px; font-weight:700; color:#5f6368; padding:8px 12px; background:#fff; border-bottom:1px solid #dadde1; text-transform:uppercase;">Social Card (WhatsApp / LinkedIn / Slack)</div>
                <img id="octo-og-image" src="{og_img_val}" style="width:100%; height:140px; object-fit:cover; display:block; background:#0f172a;" />
                <div style="padding:10px 12px;">
                    <div id="octo-og-domain" style="font-size:11px; color:#606770; text-transform:uppercase; margin-bottom:3px;">TICAPSORIGINAL.COM</div>
                    <div id="octo-og-title" style="font-size:15px; font-weight:700; color:#1d2129; line-height:1.25; margin-bottom:4px;">{og_title_val}</div>
                    <div id="octo-og-desc" style="font-size:13px; color:#606770; line-height:1.35;">{og_desc_val}</div>
                </div>
            </div>
        </div>
        """
        return mark_safe(html)

    @admin.display(description="Compiled JSON-LD Preview")
    def json_ld_preview(self, obj):
        payload = {
            "@context": "https://schema.org",
            "@type": (obj.json_ld_schema_type if obj else "") or "SoftwareApplication",
            "headline": (obj.headline_structured if obj else "") or (obj.title if obj else "") or "Django Octo SEO",
            "url": (obj.canonical_url if obj else "") or "https://ticapsoriginal.com",
            "description": (obj.description if obj else "") or "",
        }
        formatted = escape(json.dumps(payload, indent=2, ensure_ascii=False))
        return mark_safe(
            f'<pre style="background:#0f172a; color:#38bdf8; padding:12px; border-radius:6px; '
            f'font-size:12px; max-width:720px; overflow-x:auto; margin:0;">{formatted}</pre>'
        )


class SuperSEOPageAdmin(OctoSEOMetadataAdminMixin, admin.ModelAdmin):
    form = SuperSEOPageAdminForm
    list_display = (
        "page_name",
        "title",
        "seo_health_badge",
        "robots_directives",
        "json_ld_schema_type",
        "date_modified",
    )
    list_filter = (
        "robots_directives",
        "json_ld_schema_type",
        "x_frame_options",
        "language_code",
    )
    search_fields = ("page_name", "title", "description", "keywords", "canonical_url")
    readonly_fields = ("live_seo_preview", "json_ld_preview")
    save_on_top = True
    actions = ["set_index_follow", "set_noindex_nofollow", "touch_date_modified"]

    class Media:
        js = ("django_octo_seo/js/admin_seo.js",)

    fieldsets = (
        (
            "Step 1 — Essential SEO (Required)",
            {
                "fields": (
                    "page_name",
                    "title",
                    "description",
                    "canonical_url",
                    "og_image",
                    "live_seo_preview",
                ),
                "description": "Fill these core fields to optimize how your page appears on Google and social networks.",
            },
        ),
        (
            "Step 2 — Indexing & Content Details",
            {
                "fields": (
                    "robots_directives",
                    "language_code",
                    "keywords",
                    "author",
                    "thumbnail_image",
                ),
            },
        ),
        (
            "Step 3 — Custom Social Media Overrides (Optional)",
            {
                "classes": ("collapse",),
                "fields": (
                    "og_type",
                    "og_title",
                    "og_description",
                    "twitter_site",
                    "twitter_creator",
                ),
                "description": "Leave blank to automatically inherit from Step 1.",
            },
        ),
        (
            "Step 4 — Structured Data & Security (Advanced)",
            {
                "classes": ("collapse",),
                "fields": (
                    "json_ld_schema_type",
                    "headline_structured",
                    "date_published",
                    "date_modified",
                    "x_frame_options",
                    "json_ld_preview",
                ),
            },
        ),
    )

    @admin.action(description="Set visibility to Public (index, follow)")
    def set_index_follow(self, request, queryset):
        updated = queryset.update(robots_directives="index, follow")
        self.message_user(request, f"{updated} page(s) set to 'index, follow'.")

    @admin.action(description="Set visibility to Private (noindex, nofollow)")
    def set_noindex_nofollow(self, request, queryset):
        updated = queryset.update(robots_directives="noindex, nofollow")
        self.message_user(request, f"{updated} page(s) set to 'noindex, nofollow'.")

    @admin.action(description="Touch date_modified to now")
    def touch_date_modified(self, request, queryset):
        updated = queryset.update(date_modified=timezone.now())
        self.message_user(request, f"Updated modification timestamp for {updated} page(s).")


if apps.is_installed("django.contrib.admin"):
    admin.site.register(SuperSEOPage, SuperSEOPageAdmin)
