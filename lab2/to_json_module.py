def obj_to_json(obj):
    if (obj.__class__ == int) | (obj.__class__ == float):
        return "\"number\": " + str(obj)
    if obj.__class__ == str:
        return str_to_json(obj)
    if obj.__class__ == bool:
        return bool_to_json(obj)
    if obj.__class__ == list:
        return list_to_json(obj)
    if obj.__class__ == dict:
        return dict_to_json(obj)


def obj_with_key_to_json(obj, key):
    if (obj.__class__ == int) | (obj.__class__ == float):
        return "\"" + key + "\": " + str(obj)
    if obj.__class__ == str:
        return str_to_json(obj, key)
    if obj.__class__ == bool:
        return bool_to_json(obj, key)
    if obj.__class__ == list:
        return list_to_json(obj, key)
    if obj.__class__ == dict:
        return dict_to_json(obj, key)


def str_to_json(obj, key="string"):
    return "\"" + key + "\": \"" + obj + "\""


def bool_to_json(obj, key="boolean"):
    return "\"" + key + "\": " + str(obj).lower()


def list_to_json(obj, key="array"):
    string = "\"" + key + "\": [\n"
    for i in range(0, len(obj) - 1):
        string += obj_to_json(obj[i]) + ",\n"
    string += obj_to_json(obj[len(obj) - 1]) + "\n]"
    return string


def dict_to_json(obj, key="object"):
    string = "\"" + key + "\": {\n"
    for key in dict(obj).keys():
        string += obj_with_key_to_json(obj[key], key) + ",\n"
    string = string[:(len(string) - 2)] + string[(len(string) - 2):].replace(",\n", "")
    string += "\n}"
    return string
