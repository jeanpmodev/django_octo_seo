import json
import re
import pytest
from django.core.management import call_command
from django.urls import reverse


@pytest.mark.django_db
def test_no_pending_migrations():
    call_command("makemigrations", "--check", "--dry-run")


@pytest.mark.django_db
def test_seo_demo_renders_in_single_query(client, django_assert_num_queries):
    url = reverse("django_octo_seo:showcase")
    client.get(url)

    with django_assert_num_queries(1):
        response = client.get(url)

    assert response.status_code == 200
    assert response.headers.get("X-Frame-Options") in ("DENY", "SAMEORIGIN")


@pytest.mark.django_db
def test_json_ld_is_valid_and_xss_safe(client):
    response = client.get(reverse("django_octo_seo:showcase"))
    html = response.content.decode("utf-8")

    match = re.search(
        r'<script type="application/ld\+json">(.*?)</script>',
        html,
        re.DOTALL,
    )
    assert match is not None, "JSON-LD block not found in <head>."

    payload = json.loads(match.group(1))
    schemas = payload if isinstance(payload, list) else [payload]

    assert len(schemas) >= 1
    assert all("@type" in item for item in schemas)
    assert "<script>" not in json.dumps(payload)
    assert all(item.get("@context") == "https://schema.org" for item in schemas)

