# django_octo_seo

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.11+-blue)](https://python.org)
[![Framework: Django](https://img.shields.io/badge/Framework-Django-darkgreen)](https://djangoproject.com)
[![Package Manager: Rye](https://img.shields.io/badge/Package_Manager-Rye-orange)](https://astral.sh)
![PyPI Version](https://img.shields.io/pypi/v/django-octo-seo)
[![Latest on Django Packages](https://img.shields.io/badge/Django_Packages-django__octo__seo-8c3c26.svg)](https://djangopackages.org/packages/p/django-faq/)
[![Tests: pytest](https://img.shields.io/badge/Tests-pytest%20passed-2ea44f.svg)](https://github.com/jeanpmodev/django_octo_seo/blob/main/TESTING.md)
[![BDD: Behave](https://img.shields.io/badge/BDD-Behave%20verified-009688.svg)](https://github.com/jeanpmodev/django_octo_seo/blob/main/TESTING.md)
[![Load Test: Locust](https://img.shields.io/badge/Load_Test-11ms_median_%7C_0%25_fails-blueviolet.svg)](https://github.com/jeanpmodev/django_octo_seo/blob/main/performance/locust_load_report.pdf)
[![CI](https://img.shields.io/github/actions/workflow/status/jeanpmodev/django_octo_seo/ci.yml?branch=main&label=CI)](https://github.com/jeanpmodev/django_octo_seo/actions/workflows/ci.yml)


**django_octo_seo** is a production-grade, high-performance SEO injection engine designed for scalable web infrastructures. It serves as a core decoupled module under the **Django-Octo** structural framework ecosystem.

This module guarantees strict database-to-head tag integrity, mapping dynamic SEO objects straight from a pre-populated PostgreSQL/SQLite layer directly into a semantic HTML5 rendering pipeline in a single database lookup.

---

## 🔑 Key Architectural Features

- **Unified Bot Controller:** Replaced fragmented crawler instructions (`Googlebot`, `Bingbot`, `Yandex`, `Baidu`) with an optimized single-pass meta-tag runtime execution.
- **Single-Block JSON-LD Graphs:** Automated structural parsing of schema datasets (`WebSite`, `BlogPosting`) packaged into a single script rendering block to improve parsing speed.
- **Absolute URL Context Binding:** Native cross-origin preview validation utilizing Django's schema handling (`request.scheme`) to prevent media preview degradation across international CDNs and messaging APIs (WhatsApp, Slack, LinkedIn).
- **Rye Environment Integration:** Fully integrated with the ultra-fast Rust-based Python package manager for reliable dependency locks.

---

## 📋 The 8-Layer SEO & Security Matrix

The architecture exposes **8 distinct, highly optimized matrix layers** linked directly from the model fields to the client-side browser document metadata container:

| Metric ID | Component Classification | Target Tag Structure | Engineering Objective |
| :---: | :--- | :--- | :--- |
| **01** | **Security Layer** | `X-Frame-Options` | Enforces clickjacking protection natively at the document head layer. |
| **02** | **Semantic Web Core** | `<title>` | Length-validated dynamic node mapping to maximize CTR on SERPs. |
| **03** | **Indexer Snippet** | `meta name="description"` | Explicit boundary-filtered string constraint avoiding automated truncation. |
| **04** | **Multi-Crawler Policy** | `meta name="robots"` | Unifies multi-bot index/follow indicators into a single parsing execution. |
| **05** | **Link Authority** | `link rel="canonical"` | Hardlocks root canonical routing mappings to prevent scrapers from draining link juice. |
| **06** | **Micro-Format Asset** | `meta name="thumbnail"` | Pre-cached index target specifying the explicit site thumbnail icon context. |
| **07** | **Social Semantic Graph** | `og:*` & `twitter:*` | Automated layout sync mapping semantic social objects directly to Open Graph APIs. |
| **08** | **Structured Dataset** | `application/ld+json` | Injects valid Rich Results syntax validating organization and content profiles. |

---

## ⚡ Installation & Quick Start (PyPI)

Install the official package directly into any modern Django (`>=6.1.2`) and Python (`>=3.12`) infrastructure using **pip** or **Rye**:

### 1. Install Package
```bash
pip install django-octo-seo
```
Or using the Rust-backed **Rye** package manager:
```bash
rye add django-octo-seo
```

### 2. Register App & Migrate
Add `"django_octo_seo"` to `INSTALLED_APPS` in your `settings.py`:
```python
INSTALLED_APPS = [
    # ...
    "django_octo_seo",
]
```
Apply the database schema migrations:
```bash
python3 manage.py migrate
```

### 3. Mount the Showcase Endpoint
Include the self-contained module routes in your main `urls.py`:
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("seo-demo/", include("django_octo_seo.urls")),
]
```
Start the server (`python3 manage.py runserver`) and navigate to `http://127.0.0.1:8000` to inspect the live semantic HTML5 and JSON-LD head layer rendered via a single database lookup.

---

## ⚙️ Local Sandbox & Development Setup (Using Rye)

This repository keeps local database binaries excluded from version control to ensure clean environment isolation. You can initialize a fresh local SQLite schema directly via Django migrations.

### 1. Clone & Synchronize Environment
Clone the repository and trigger the Rust-backed Rye environment compiler to lock and synchronize dependencies:
```bash
git clone https://github.com/jeanpmodev/django_octo_seo.git
cd django_octo_seo
rye sync
```

### 2. Initialize Runtime Service
Fire up the local development engine instance:
```bash
python3 manage.py runserver
```
Navigate to `127.0.0.1:8000` to inspect the structural head layer live.

---

## 🧪 Quality Assurance & Testing

This module is backed by a dedicated QA suite covering **Unit & Query-Count Tests (`pytest`)**, **BDD Specifications (`behave`)**, and **Load Testing (`locust`)**. To keep the core package minimal, test dependencies are installed on demand—see [TESTING.md](TESTING.md) for instructions and benchmark reports.


## 📄 License & Ecosystem Blueprint

Distributed under the permissive terms of the **MIT License**. 

`django_octo_seo` is an open-source structural sub-module developed for the **Django-Octo** architecture. For deep technical insights regarding enterprise database design, professional networking data, and global IT sectors, please explore our platform documentation at [ticapsoriginal.com](https://ticapsoriginal.com).
