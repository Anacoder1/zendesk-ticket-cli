import os

AUTH_EMAIL = os.getenv("ZENDESK_EMAIL")
AUTH_PASSWORD = os.getenv("ZENDESK_PASSWORD")
SUPPORT_BASE_URL = os.getenv("ZENDESK_URL")

if None in [AUTH_EMAIL, AUTH_PASSWORD, SUPPORT_BASE_URL]:
    raise ValueError("Environment variables not set correctly!")
