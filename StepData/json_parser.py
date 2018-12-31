import json


def get_data(path):
    result = []
    json_obj = json.load(open(path))
    data_obj = json.loads(json_obj['data'])
    for i in range(len(data_obj)):
        result.append(json.loads(data_obj[i]))
    return result, int(json_obj['stepNumbers'])
