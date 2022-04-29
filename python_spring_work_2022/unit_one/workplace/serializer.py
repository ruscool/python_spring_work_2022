import pickle, json, yaml


def to_pickle(obj, file):
    """
    Запись файла в Pickle формат w+b
    :param obj:
    :param file:

    """
    fd = open(file, "w+b")
    pickle.dump(obj, fd, pickle.HIGHEST_PROTOCOL)
    fd.close()



def to_json(obj, file):
    """
    Запись файла в Json формат
    :param obj:
    :param file:
    :return:
    """
    with open(file, "wt") as f:
        json.dump(obj, f, indent=4)
    return print("write in json ok")


def to_yaml(obj, file):
    """
    Запись файла в Yaml
    :param obj:
    :param file:
    :return:
    """
    with open(file, "wt") as f:
        yaml.dump(obj, f)
    return print("write in yaml ok")
