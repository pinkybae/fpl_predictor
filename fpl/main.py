import requests
from core.utils import CustomLogger
# from db.connect import save_to_db

URL = "https://fantasy.premierleague.com/api/bootstrap-static/"
log = CustomLogger()

def get_all_data() -> dict:
    try:
        log.start("get_all_data")
        resp = requests.get(URL)
        resp_json = resp.json()
        log.info('get_all_data :: Following data received :: {}'.format(list(resp_json.keys())))
        log.end("get_all_data")
        return resp_json
    except Exception as e:
        log.error('get_all_data :: Failed to Fetch Data :: {}'.format(e))
        raise Exception