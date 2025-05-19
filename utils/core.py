import requests

BASE_URL = "https://www.mytranslator.com"

def get_translation(word, locale):
    return requests.get(BASE_URL, params={"query": word, "locale": locale})
