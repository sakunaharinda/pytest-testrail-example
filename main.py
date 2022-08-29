import os
from testrail_api import TestRailAPI
from pprint import pprint

if __name__=='__main__':
    url = "https://sakuna.testrail.io/"
    email = os.environ['TESTRAIL_USER']
    pw = os.environ['TESTRAIL_KEY']

    # project_id = 10
    # plan_id = 520
    # suit_id = 17
    # run_id = 521

    project_id = 2
    plan_id = 14
    suit_id = 2
    run_id = 15

    api = TestRailAPI(url=url, email=email, password=pw)
    pprint(api.suites.get_suites(project_id))
