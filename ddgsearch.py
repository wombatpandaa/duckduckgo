# query ddg api for "presidents of the united states"
# test that each president is listed in the response by last name using pytest
# use github repository as scc
# use travis cl to continuously test as changes are pushed

import requests
import pytest

url = 'http://api.duckduckgo.com/?q=presidents+of+the+united+states&format=json&pretty=1'

response = requests.get(url)

json_data = response.json()

related_topics_list = json_data['RelatedTopics']

text_list = []
for topic in related_topics_list:
    text_list.append(topic['Text'])

test_list = {
    'Washington',
    'Adams',
    'Jefferson',
    'Madison',
    'Monroe',
    'Adams',
    'Jackson',
    'Buren',
    'Harrison',
    'Tyler',
    'Polk',
    'Taylor',
    'Fillmore',
    'Pierce',
    'Buchanan',
    'Lincoln',
    'Johnson',
    'Grant',
    'Hayes',
    'Garfield',
    'Arthur',
    'Cleveland',
    'Harrison',
    'McKinley',
    'Roosevelt',
    'Taft',
    'Wilson',
    'Harding',
    'Coolidge',
    'Hoover',
    'Truman',
    'Eisenhower',
    'Kennedy',
    'Johnson',
    'Nixon',
    'Ford',
    'Carter',
    'Reagan',
    'Bush',
    'Clinton',
    'Obama',
    'Trump',
    'Biden'
}

for string in text_list:
    assert any(x in test_list for x in string)
