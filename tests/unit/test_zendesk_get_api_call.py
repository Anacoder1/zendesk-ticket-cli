from zendesk.utils.helpers import zendesk_get_api_call
from zendesk.utils.config import SUPPORT_BASE_URL, AUTH_EMAIL, AUTH_PASSWORD


def test_zendesk_get_api_call():
    testcases = [
        {
            "url": "something.zendesk.com",
            "empty_response": True,
        },
        {
            "url": "https://zccanaxyz1.zendesk.com/api/v2/tickets/25.json",
            "empty_response": False,
        },
    ]

    for t in testcases:
        resp = zendesk_get_api_call(t.get("url"), AUTH_EMAIL, AUTH_PASSWORD)
        if t.get("empty_response"):
            assert resp == None
        else:
            assert resp != None
