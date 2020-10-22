import requests
import pytest
import contains

url_ddg = "https://api.duckduckgo.com"
resp = requests.get(url_ddg + "/?q=presidents+of+the+united+states&format=json")
rsp_data = resp.json()
x = 0
rsp_list = []
while x < 52:
    rsp_list.append(rsp_data["RelatedTopics"][x]["Text"])
    x = x + 1


@pytest.mark.parametrize("pres", ['Washington', 'Adams', 'Jefferson', 'Madison',
                                  'Monroe', 'Adams', 'Jackson', 'Buren', 'Harrison',
                                  'Tyler', 'Polk', 'Taylor', 'Fillmore', 'Pierce',
                                  'Buchanan', 'Lincoln', 'Johnson', 'Grant', 'Hayes',
                                  'Garfield', 'Arthur','Cleveland', 'Harrison',
                                  'Cleveland', 'McKinley', 'Roosevelt', 'Taft', 'Wilson',
                                  'Harding', 'Coolidge', 'Hoover', 'Roosevelt', 'Truman',
                                  'Eisenhower','Kennedy', 'Johnson', 'Nixon', 'Ford',
                                  'Carter', 'Reagan', 'Bush', 'Clinton','Bush',
                                  'Obama', 'Trump'])
def test_duckduckgo(pres):

     assert contains.contains(pres, rsp_list) == 1