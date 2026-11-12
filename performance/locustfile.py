from locust import HttpUser, between, task


class SeoCrawlerUser(HttpUser):
    wait_time = between(0.5, 2.0)

    @task(3)
    def access_seo_demo_page(self):
        with self.client.get(
            "/",
            headers={"User-Agent": "Mozilla/5.0 (compatible; Googlebot/2.1)"},
            catch_response=True,
        ) as response:
            if response.status_code != 200:
                response.failure(f"HTTP failure: {response.status_code}")
            elif "application/ld+json" not in response.text:
                response.failure("JSON-LD missing under load")
            else:
                response.success()

    @task(1)
    def access_with_utm_params(self):
        self.client.get("/?utm_source=linkedin&utm_medium=social")
