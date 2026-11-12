Feature: SEO Matrix and Structured Data
  As a search engine crawler or social network parser
  I want to read semantic and secure metadata in the <head>
  In order to index and preview the page accurately

  Scenario: Render showcase page with security headers and JSON-LD
    Given the system is online
    When a visitor accesses the "/seo-demo/" route
    Then the response status code should be 200
    And the HTTP header "X-Frame-Options" should be present
    And the page should contain the "og:title" meta tag
    And the JSON-LD script should contain the "https://schema.org" context

