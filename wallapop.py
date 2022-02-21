import requests
import constants as Constants
from aux import headers_http_get, headers_http_put, generate_body_json


def get_all_product_ids():
    product_ids = []
    url = f'{Constants.BASE_URL}/web/items/mine/published?init=0'
    resp = requests.get(url, headers=headers_http_get("items/mine/published",))
    if resp.status_code == 200:
        product_ids = [e['id'] for e in resp.json()]
    return product_ids


def get_user_data():
    url = f'{Constants.BASE_URL}/users/{Constants.USER_ID}'
    resp = requests.get(url)
    if resp.status_code == 200:
        return resp.json()
    else:
        return None


def update_product(product_id):
    url = f'{Constants.BASE_URL}/items/{product_id}'
    data = generate_body_json(item_data=requests.get(
        url+'/vertical').json(), user_data=get_user_data())
    resp = requests.put(url, headers=headers_http_put(),
                        data=data.encode('utf-8'))
    if (resp.status_code != 200):
        print(data)
    return resp.status_code
