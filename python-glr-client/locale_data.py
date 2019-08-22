
import json
import locale
import os

PLAIN_STRING = 'plain_string'
DATE = 'date'
TIME = 'time'
DATETIME = 'datetime'
AMOUNT = 'amount'
DISTANCE = 'distance'
SPEED = 'speed'


def check_required_params(msg_params, given_params={}):
    params = dict()
    for keyword, keyword_type in msg_params.items():
        value = given_params[keyword]
        if keyword in given_params:
            if keyword_type == PLAIN_STRING:
                params[keyword] = value
            elif keyword_type == DATE:
                params[keyword] = value.strftime('%B %d, %Y')
            elif keyword_type == TIME:
                params[keyword] = value.strftime('%H:%M:%S')
            elif keyword_type == DATETIME:
                params[keyword] = value.strftime('%B %d, %Y %H:%M:%S')
            elif keyword_type == AMOUNT:
                # TODO Localise Amount in given locale
                params[keyword] = str(value)
            elif keyword_type == DISTANCE:
                # TODO Localise and (Convert) Distance in given locale
                params[keyword] = str(value)
            elif keyword_type == SPEED:
                # TODO Localise and (Convert) Speed in given locale
                params[keyword] = str(value)
            else:
                params[keyword] = str(value)
        else:
            params[keyword] = ''
    return params


def get_message_string(msg_id, platform_name, locale_lang, **kwargs):
    if not locale_lang:
        locale_lang = 'es-US'
    locale.setlocale(locale.LC_ALL, locale_lang.replace('-', '_'))
    path = os.path.dirname(os.path.realpath(__file__))
    if not locale_lang:
        locale_lang = 'en-US'
    json_file = path + '/MessageString/' + locale_lang + '.json'
    with open(json_file, 'r') as msg_data_file:
        msg_data = json.loads(msg_data_file.read())
    msg_str = msg_data['msg_data'][platform_name][msg_id]['msg_str']
    msg_params = msg_data['msg_data'][platform_name][msg_id]['msg_params']
    required_params = check_required_params(msg_params, kwargs)
    msg_str = msg_str.format(**required_params)
    return msg_str
