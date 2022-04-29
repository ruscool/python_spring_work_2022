import pickle, json, yaml


def from_pickle(file):
    with open(file, "rb") as f:
        obj = pickle.load(f)
    #print(obj)  # проверка объекта
    return obj


def from_json(file):
    with open(file, "rt") as f:
        obj = json.load(f)
    print(obj)


def from_yaml(file):
    with open(file, "wt") as f:
        obj = yaml.load(f)
    print(obj)
