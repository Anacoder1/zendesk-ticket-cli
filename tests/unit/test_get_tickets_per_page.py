from zendesk.utils.helpers import get_tickets_per_page_and_return_next_page


def test_zendesk_get_api_call():
    testcases = [
        {
            "page_url": "https://zccanaxyz1.zendesk.com/api/v2/tickets?page[size]=25",
            "expected_tickets": 25,
        },
        {
            "page_url": "https://zccanaxyz1.zendesk.com/api/v2/tickets?page[size]=32",
            "expected_tickets": 32,
        },
        {
            "page_url": "https://zccanaxyz1.zendesk.com/api/v2/tickets?page[size]=abc",
            "expected_tickets": 0,
        }
    ]

    for t in testcases:
        resp, _ = get_tickets_per_page_and_return_next_page(t.get("page_url"))
        assert len(resp) == t.get("expected_tickets")
