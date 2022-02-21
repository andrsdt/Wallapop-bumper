import requests
import constants as Constants
from aux import headers_http_get, headers_http_put, generate_body_json
import colors as Colors


def get_all_product_ids():
    product_ids = []
    offset = 0
    has_next = True

    # The results are paginated, so we need to iterate over all the pages (size 20)
    while has_next:
        url = f'{Constants.BASE_URL}/web/items/mine/published?init={offset}'
        resp = requests.get(
            url, headers=headers_http_get("items/mine/published",))
        if resp.status_code == 200:
            fetched_product_ids = [e['id'] for e in resp.json()]
            product_ids += fetched_product_ids
            has_next = len(fetched_product_ids) == 20
            offset += 20
        else:
            print(Colors.RED + "Error getting product ids from " + url)
            break

    print(Colors.BLUE + f'{len(product_ids)} products found')
    if (len(product_ids) == 0):
        print(Colors.BLUE + "If you have products published, please create the .env file according to the instructions in README.md")
    return product_ids


def get_user_data():
    url = f'{Constants.BASE_URL}/users/{Constants.USER_ID}'
    resp = requests.get(url)
    if resp.status_code == 200:
        return resp.json()
    else:
        print(Colors.RED + "Error getting user data from " + url)


def update_product(product_id):
    url = f'{Constants.BASE_URL}/items/{product_id}'
    data = generate_body_json(item_data=requests.get(
        url+'/vertical').json(), user_data=get_user_data())

    if (data == None):
        # Skip this product if there was an error generating the body JSON
        return

    resp = requests.put(url, headers=headers_http_put(),
                        data=data.encode('utf-8')
                        )

    color = Colors.GREEN if resp.status_code == 200 else Colors.RED
    print(f'{color}id: {product_id}\tcode: {resp.status_code}')
