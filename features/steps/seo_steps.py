import json
import re
from behave import given, then, when
from django.test import Client


@given("the system is online")
def step_system_online(context):
    context.client = Client()


@when('a visitor accesses the "{route}" route')
def step_visit_route(context, route):
    context.response = context.client.get(route)
    context.html = context.response.content.decode("utf-8")


@then("the response status code should be {status_code:d}")
def step_check_status(context, status_code):
    assert context.response.status_code == status_code


@then('the HTTP header "{header_name}" should be present')
def step_check_header(context, header):
    assert header in context.response.headers


@then('the page should contain the "{meta_name}" meta tag')
def step_check_og_tag(context, property_name):
    assert f'property="{property_name}"' in context.html


@then('the JSON-LD script should contain the "{schema_url}" context')
def step_check_json_ld(context, schema_url):
    match = re.search(
        r'<script type="application/ld\+json">(.*?)</script>',
        context.html,
        re.DOTALL,
    )
    assert match is not None
    data = json.loads(match.group(1))
    schemas = data if isinstance(data, list) else [data]
    assert any(item.get("@context") == schema_url for item in schemas)

