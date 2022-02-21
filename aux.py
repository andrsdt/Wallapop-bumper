from wallapop_signature import generate_xsignature
import time
import json
import constants as Constants


def headers_http_put():
    return {
        'Connection': 'keep-alive',
        'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
        'DNT': '1',
        'X-DeviceOS': '0',
        'Accept-Language': 'es,en-US;q=0.9,es-ES;q=0.8,en;q=0.7',
        'sec-ch-ua-mobile': '?0',
        'Authorization': Constants.BEARER_AUTHORIZATION,
        'Content-Type': 'application/json',
        'Accept': 'application/json, text/plain, */*',
        'DeviceOS': '0',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
        'sec-ch-ua-platform': '"Linux"',
        'Origin': 'https://es.wallapop.com',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://es.wallapop.com/',
    }


def headers_http_get(endpoint):
    headers = {
        'Connection': 'keep-alive',
        'DeviceID': '',
        'X-Signature': None,
        'DNT': '1',
        'Accept-Language': 'es_ES,en-US;q=0.9,es-ES;q=0.8,es;q=0.7,en;q=0.6',
        'sec-ch-ua-mobile': '?0',
        'Authorization': Constants.BEARER_AUTHORIZATION,
        'Accept': 'application/json, text/plain, */*',
        'Timestamp': None,
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
        'sec-ch-ua-platform': '"Linux"',
        'Origin': 'https://es.wallapop.com',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://es.wallapop.com/',
    }
    current_time_str = str(time.time())
    headers['Timestamp'] = current_time_str
    headers['X-Signature'] = generate_xsignature(
        endpoint, "GET", current_time_str)
    return headers


def blank_space_treatment(string):
    # if the last element of a string is a blank space, remove it. Else, add it
    # this is to slightly modify the description of the item every time, just in case it matters
    if string[-1] == " ":
        return string[:-1]
    else:
        return string + " "


def generate_body_json(item_data, user_data):
    # item_data is a json with the data of the item obtained via http get
    # user_data is a json with the data of the user obtained via http get
    content = item_data['content']
    body = {
        'id': item_data['id'],
        'category_id': str(content['category_id']),
        'title': content['title'],
        'sale_price': int(content['sale_price']),
        'currency_code': content['currency_code'],
        'description': blank_space_treatment(content['description']),
        'sale_conditions': content['sale_conditions'],
        'delivery_info': {
            'min_weight_kg': int(content['delivery_info']['min_weight_kg']),
            'max_weight_kg': int(content['delivery_info']['max_weight_kg']),
            'location': {
                'address': f'{user_data["location"]["zip"]}, {user_data["location"]["city"]}',
                'latitude': user_data['location']['approximated_latitude'],
                'longitude': user_data['location']['approximated_longitude']
            }
        }
    }
    # missing 'extraInfo', it's not mandatory
    return json.dumps(body)
