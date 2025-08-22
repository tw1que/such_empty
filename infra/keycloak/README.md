# Keycloak Setup (Optional)

This folder contains notes for running a local Keycloak instance for OIDC development.

1. Download the Keycloak container image.
2. Create a realm named `inventory` and a client `inventory-frontend`.
3. Update `.env` with the issuer URL and client details.

Keycloak integration is optional; the backend accepts a mock bearer token when `OIDC_ENABLED=false`.
