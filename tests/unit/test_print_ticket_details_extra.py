from zendesk.utils.helpers import print_ticket_details_extra
from zendesk.utils.config import SUPPORT_BASE_URL, AUTH_EMAIL, AUTH_PASSWORD

def test_print_ticket_details_extra(capfd):
    test_cases = [
        {
        "ticket": {'url': 'https://zccanaxyz1.zendesk.com/api/v2/tickets/25.json', 'id': 25, 'external_id': None, 'via': {'channel': 'api', 'source': {'from': {}, 'to': {}, 'rel': None}}, 'created_at': '2021-11-26T00:00:55Z', 'updated_at': '2021-11-26T00:00:55Z', 'type': None, 'subject': 'voluptate dolor deserunt ea deserunt', 'raw_subject': 'voluptate dolor deserunt ea deserunt', 'description': 'Consectetur eiusmod pariatur ullamco voluptate irure sunt magna cillum velit irure commodo culpa ipsum in. Nulla non exercitation dolor quis minim deserunt ad consequat officia ullamco irure consectetur anim mollit. Cupidatat exercitation cillum excepteur culpa consectetur ad adipisicing exercitation est amet ullamco id eiusmod tempor. Aliqua quis irure culpa tempor mollit veniam. Fugiat aliquip duis non sit id eu ea anim sit ea aliqua et dolor.\n\nCulpa culpa culpa id proident dolor magna ipsum dolor irure mollit proident culpa. Officia Lorem veniam dolor sit commodo id consequat ex qui enim veniam. Laboris velit excepteur sit sit anim nulla exercitation.', 'priority': None, 'status': 'open', 'recipient': None, 'requester_id': 1902326529344, 'submitter_id': 1902326529344, 'assignee_id': 1902326529344, 'organization_id': 1900081685144, 'group_id': 4411212176539, 'collaborator_ids': [], 'follower_ids': [], 'email_cc_ids': [], 'forum_topic_id': None, 'problem_id': None, 'has_incidents': False, 'is_public': True, 'due_at': None, 'tags': ['do', 'est', 'labore'], 'custom_fields': [], 'satisfaction_rating': None, 'sharing_agreement_ids': [], 'fields': [], 'followup_ids': [], 'ticket_form_id': 1900004186464, 'brand_id': 1900001329924, 'allow_channelback': False, 'allow_attachments': True},
        "expected_output": """╒══════╤═══════════════╤════════════════╤═══════════════╤════════╤══════════════════════╤══════════════════════╤══════════════════════════════════════╤═════════════════╕
│   ID │   Assignee_ID │   Requester_ID │      Group_ID │ Type   │ Created At           │ Updated At           │ Subject                              │ Tags            │
╞══════╪═══════════════╪════════════════╪═══════════════╪════════╪══════════════════════╪══════════════════════╪══════════════════════════════════════╪═════════════════╡
│   25 │ 1902326529344 │  1902326529344 │ 4411212176539 │        │ 2021-11-26T00:00:55Z │ 2021-11-26T00:00:55Z │ voluptate dolor deserunt ea deserunt │ do, est, labore │
╘══════╧═══════════════╧════════════════╧═══════════════╧════════╧══════════════════════╧══════════════════════╧══════════════════════════════════════╧═════════════════╛

------------- Additional data -------------

DESCRIPTION:
Consectetur eiusmod pariatur ullamco voluptate irure sunt magna cillum velit irure commodo culpa ipsum in. Nulla non exercitation dolor quis minim deserunt ad consequat officia ullamco irure consectetur anim mollit. Cupidatat exercitation cillum excepteur culpa consectetur ad adipisicing exercitation est amet ullamco id eiusmod tempor. Aliqua quis irure culpa tempor mollit veniam. Fugiat aliquip duis non sit id eu ea anim sit ea aliqua et dolor.

Culpa culpa culpa id proident dolor magna ipsum dolor irure mollit proident culpa. Officia Lorem veniam dolor sit commodo id consequat ex qui enim veniam. Laboris velit excepteur sit sit anim nulla exercitation.

╒═══════════════════════════════════════════════════════╤═══════════════════╤══════════════════╤════════════════╕
│ URL                                                   │   Organization ID │   Ticket Form ID │   Submitter ID │
╞═══════════════════════════════════════════════════════╪═══════════════════╪══════════════════╪════════════════╡
│ https://zccanaxyz1.zendesk.com/api/v2/tickets/25.json │     1900081685144 │    1900004186464 │  1902326529344 │
╘═══════════════════════════════════════════════════════╧═══════════════════╧══════════════════╧════════════════╛"""
        },
        {
        "ticket": {'url': 'https://zccanaxyz1.zendesk.com/api/v2/tickets/10.json', 'id': 10, 'external_id': None, 'via': {'channel': 'api', 'source': {'from': {}, 'to': {}, 'rel': None}}, 'created_at': '2021-11-26T00:00:48Z', 'updated_at': '2021-11-26T00:00:48Z', 'type': None, 'subject': 'magna reprehenderit nisi est cillum', 'raw_subject': 'magna reprehenderit nisi est cillum', 'description': 'Sit sit consequat magna aliquip officia qui. Fugiat amet id dolor sint exercitation sit. Eiusmod ex eiusmod voluptate voluptate est amet non culpa minim enim minim. Eiusmod fugiat veniam duis eiusmod sint laborum ex amet occaecat.\n\nNostrud consequat officia tempor amet eu. Non adipisicing dolore amet minim id consequat labore irure in esse et aliqua pariatur. Aliquip aliqua id ipsum amet laboris exercitation sunt cillum est et est. Tempor amet qui do dolore fugiat ad id nulla ullamco dolore tempor irure deserunt magna. Ipsum voluptate aliquip ut ad in pariatur adipisicing occaecat ea excepteur Lorem enim exercitation. Lorem sunt officia voluptate pariatur labore esse nostrud ullamco irure sit. Voluptate exercitation do aliquip eu consectetur.', 'priority': None, 'status': 'open', 'recipient': None, 'requester_id': 1902326529344, 'submitter_id': 1902326529344, 'assignee_id': 1902326529344, 'organization_id': 1900081685144, 'group_id': 4411212176539, 'collaborator_ids': [], 'follower_ids': [], 'email_cc_ids': [], 'forum_topic_id': None, 'problem_id': None, 'has_incidents': False, 'is_public': True, 'due_at': None, 'tags': ['aliquip', 'magna', 'non'], 'custom_fields': [], 'satisfaction_rating': None, 'sharing_agreement_ids': [], 'fields': [], 'followup_ids': [], 'ticket_form_id': 1900004186464, 'brand_id': 1900001329924, 'allow_channelback': False, 'allow_attachments': True},
        "expected_output": """╒══════╤═══════════════╤════════════════╤═══════════════╤════════╤══════════════════════╤══════════════════════╤═════════════════════════════════════╤═════════════════════╕
│   ID │   Assignee_ID │   Requester_ID │      Group_ID │ Type   │ Created At           │ Updated At           │ Subject                             │ Tags                │
╞══════╪═══════════════╪════════════════╪═══════════════╪════════╪══════════════════════╪══════════════════════╪═════════════════════════════════════╪═════════════════════╡
│   10 │ 1902326529344 │  1902326529344 │ 4411212176539 │        │ 2021-11-26T00:00:48Z │ 2021-11-26T00:00:48Z │ magna reprehenderit nisi est cillum │ aliquip, magna, non │
╘══════╧═══════════════╧════════════════╧═══════════════╧════════╧══════════════════════╧══════════════════════╧═════════════════════════════════════╧═════════════════════╛

------------- Additional data -------------

DESCRIPTION:
Sit sit consequat magna aliquip officia qui. Fugiat amet id dolor sint exercitation sit. Eiusmod ex eiusmod voluptate voluptate est amet non culpa minim enim minim. Eiusmod fugiat veniam duis eiusmod sint laborum ex amet occaecat.

Nostrud consequat officia tempor amet eu. Non adipisicing dolore amet minim id consequat labore irure in esse et aliqua pariatur. Aliquip aliqua id ipsum amet laboris exercitation sunt cillum est et est. Tempor amet qui do dolore fugiat ad id nulla ullamco dolore tempor irure deserunt magna. Ipsum voluptate aliquip ut ad in pariatur adipisicing occaecat ea excepteur Lorem enim exercitation. Lorem sunt officia voluptate pariatur labore esse nostrud ullamco irure sit. Voluptate exercitation do aliquip eu consectetur.

╒═══════════════════════════════════════════════════════╤═══════════════════╤══════════════════╤════════════════╕
│ URL                                                   │   Organization ID │   Ticket Form ID │   Submitter ID │
╞═══════════════════════════════════════════════════════╪═══════════════════╪══════════════════╪════════════════╡
│ https://zccanaxyz1.zendesk.com/api/v2/tickets/10.json │     1900081685144 │    1900004186464 │  1902326529344 │
╘═══════════════════════════════════════════════════════╧═══════════════════╧══════════════════╧════════════════╛"""
        }
    ]

    for t in test_cases:
        print_ticket_details_extra(t.get("ticket"))
        out, err = capfd.readouterr()
        print(t.get("expected_output"))
        out2, err = capfd.readouterr()
        assert out == out2