import requests

BASE_URL = "https://cafebazaar.ir"


def get_page(p=0, la="fa"):
    r = requests.get(BASE_URL + "{}?p={}&la={}".format("/lists/ml-top-inline-apps/", p, la))
    return r.content


def get_app(link):
    r = requests.get(BASE_URL + link)
    return r.content
