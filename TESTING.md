# 🧪 Quality Assurance & Testing Methodology

[![Tests: pytest](https://img.shields.io/badge/Tests-pytest%20passed-2ea44f.svg)](#2-unit--query-count-validation-pytest)
[![BDD: Behave](https://img.shields.io/badge/BDD-Behave%20verified-009688.svg)](#3-behavioral--bdd-specifications-behave)
[![Load Test: Locust](https://img.shields.io/badge/Load_Test-11ms_median_%7C_0%25_fails-blueviolet.svg)](performance/locust_load_report.pdf)

To preserve the **zero-bloat** philosophy of `django_octo_seo`, testing and benchmarking frameworks are intentionally excluded from `pyproject.toml` and production PyPI builds. They are installed on demand only when running the local QA suite.

---

## 1. On-Demand QA Setup
Inside an isolated virtual environment, install the validation stack:
```bash
rye add pytest pytest-django behave locust
```

---

## 2. Unit & Query-Count Validation (`pytest`)
Verifies schema migrations, HTTP clickjacking headers (`X-Frame-Options`), XSS escaping in `JSON-LD`, and enforces the **Single Database Lookup (`assertNumQueries(1)`)** contract:
```bash
PYTHONPATH=src pytest
```

---

## 3. Behavioral / BDD Specifications (`behave`)
Executes Gherkin scenarios (`features/seo_matrix.feature`) validating all semantic and security layers end-to-end:
```bash
PYTHONPATH=src behave
```

---

## 4. Load & Concurrency Stress Benchmark (`locust`)
Simulates 50 concurrent crawlers (`Googlebot/2.1` + social traffic with `UTM` parameters) hitting the live rendering endpoint:

```bash
# Terminal 1: Start runtime service
PYTHONPATH=src python3 manage.py runserver --noreload

# Terminal 2: Execute 15s headless load test
locust -f performance/locustfile.py --headless -u 50 -r 10 --run-time 15s --host http://127.0.0.1:8000
```

### Benchmark Results (50 Concurrent Users / 526 Requests)
* **Failure Rate:** `0.00%` (526/526 HTTP 200 OK with verified `application/ld+json` blocks)
* **Median Latency (50%ile):** `11 ms` (`10 ms` on UTM routes)
* **Average Latency:** `19.73 ms`
* **Throughput:** `36.59 req/s` (on single-threaded SQLite development server)

📄 **[View Official Locust Load Test Report (PDF)](performance/locust_load_report.pdf)**

