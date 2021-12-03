# Zendesk Ticket Viewer

This repository contains code, unit tests and other artifacts for my submission to Zendesk's Summer 2022 Internship challenge - **The Zendesk Ticket Viewer**.<br><br>


## Installation Instructions

Start by git-cloning the repository with the following command. This will download all the files of this project to the directory (which you'll choose) on your local system  <br>

```
git clone https://github.com/Anacoder1/zendesk_ticket_cli.git
```
<br>

Navigate to the project directory in the terminal (using `cd`) and run `python setup.py install` or `make install`.<br>

(`make install` will run on Linux / MacOS systems, while the former command `python setup.py install` can run on systems having Python installed on them)<br>



On a terminal shell, define 3 environment variables shown as follows (these details aren't real, it's shown as an example): <br>

Before every variable, make sure to prefix the command `set` (for Windows environments) or `export` (for Linux / MacOS environment) (e.g. `export ZENDESK_EMAIL = another_email_id@gmail.com`)<br>

```
ZENDESK_EMAIL = some_email_address@gmail.com
ZENDESK_URL = zccsomeuser1.zendesk.com
ZENDESK_PASSWORD = PpaSswwOoRrDd123!@#
```
<br>

**CAUTION**: These variables contain sensitive information, so be thoughtful of the development environment you're typing them in.<br><br>

## Usage

Activate the CLI with the command `zendesk`.<br>

![](https://github.com/Anacoder1/zendesk_ticket_cli/blob/master/artifacts/images/zendesk.PNG)<br>

Choosing option `1` will display all the tickets there are in the user's Zendesk account, with 25 tickets per page.<br>

At the end of each page, the user has the option of choosing if he/she wishes to view the next page of tickets (if option `y` is chosen)...<br>

![](https://github.com/Anacoder1/zendesk_ticket_cli/blob/master/artifacts/images/testing%20option%201.PNG)<br>

...or not (option `n` is chosen).<br>

![](https://github.com/Anacoder1/zendesk_ticket_cli/blob/master/artifacts/images/testing%20option%201%20Part%202.PNG)<br><br>

If a user reaches the last page of tickets, the CLI would show that all tickets have been covered.<br>

![](https://github.com/Anacoder1/zendesk_ticket_cli/blob/master/artifacts/images/all%20tickets%20covered.PNG)<br><br>

Choosing option `2` will display various details about a specific ticket, selected by the ticket ID.<br>

![](https://github.com/Anacoder1/zendesk_ticket_cli/blob/master/artifacts/images/testing%20option%202.PNG)<br><br>

In case the environment variables were set incorrectly, the following error is thrown.<br>

![](https://github.com/Anacoder1/zendesk_ticket_cli/blob/master/artifacts/images/couldn't%20authenticate.PNG)<br>

A similar error would be thrown in case the API is unavailable due to server-side issues.<br><br>

For option `2`, if a ID of a ticket is entered which doesn't exist in the user's account, a 404 error is returned.<br>

![](https://github.com/Anacoder1/zendesk_ticket_cli/blob/master/artifacts/images/testing%20option%202%20wrong%20input.PNG)<br><br>

And finally, when a user's done using the ticket-viewer CLI, he/she can exit using option `3`.<br>

![](https://github.com/Anacoder1/zendesk_ticket_cli/blob/master/artifacts/images/testing%20option%203.PNG)<br><br>

Until a user specifically wishes to exit (using option `3`), they'll be repeatedly prompted for input after the results of the previous query have been displayed.<br><br>

## Testing

Unit tests have been written for 5 functions and the total code coverage for the project is **97%**.<br>

Tests can be run with `py.test tests/unit/test_*.py` (from the main project directory) or `coverage run -m pytest tests/unit/test_*.py` (requires `coverage` and `pytest` Python libraries to be installed).<br>

![](https://github.com/Anacoder1/zendesk_ticket_cli/blob/master/artifacts/images/all%20tests%20passed.PNG)<br><br>

The coverage report could be viewed using `coverage report -m`<br>

![](https://github.com/Anacoder1/zendesk_ticket_cli/blob/master/artifacts/images/coverage%20report.PNG)<br><br>

## Appendix

Unlike many other versions of `ticket-viewer` available online, the setup for this CLI doesn't require the user to manually install the dependency libraries (using say `pip install -r requirements.txt`).<br>
Setup is as simple as running the command `python setup.py install`<br><br>

In addition, whereas most implementations might have stored the user credentials (email_id, zendesk_url, password) in a config file, secret file, etc., this implementation doesn't store them anywhere - it simply asks the user to enter the details by defining environment variables, which get removed automatically once the session is closed.<br>

The `Makefile` contains other commands of interest regarding setup and testing.<br><br>

Sample Zendesk tickets are contained in the `tickets.json` file.

The following code snippet bulk loads the tickets in `tickets.json` to a user's Zendesk account.<br>

```
import json

user = some_email_address@gmail.com
pwd = PpaSswwOoRrDd123!@#

file_object = open('tickets.json')
tickets_data = json.load(file_object)

payload = json.dumps(tickets_data)

url = 'https://zccsomeuser1.zendesk.com/api/v2/imports/tickets/create_many.json'
headers = {'content-type': 'application/json'}

response = requests.post(url, data = payload, auth = (user, pwd), headers = headers)
```
<br>

### Author Details

`Name`: Anamitra Musib<br>

`Email`: ana1998musib+zendesk@gmail.com<br>

***