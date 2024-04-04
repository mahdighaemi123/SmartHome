import json


def add_params_to_url(url, params):
    if len(params.keys()) > 0:
        url += "?"

        for index, key in enumerate(params.keys()):

            value = params[key]

            if isinstance(value, (dict, list)):
                value = json.dumps(value)

            url += f'{key}={value}'

            if index < len(params.keys()) - 1:
                url += "&"
    return url
