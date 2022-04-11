import json


def dict2json(dictx: dict, indent=4):
    dict_new = {
        k: v if isinstance(v, (bool, tuple, dict, float, int)) else str(v)
        for k, v in dictx.items()
    }

    return json.dumps(dict_new, ensure_ascii=False, indent=indent)


pass
