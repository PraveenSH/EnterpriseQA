import json


def LoadAppsInfo():

    info_path = "/Users/praveen/Enterprise_QA/data/apps_info.json"
    info_data = json.load(open(info_path, 'r'))
    return info_data


def LoadTasksInfo():

    info_path = "/Users/praveen/Enterprise_QA/data/tasks_info.json"
    info_data = json.load(open(info_path, 'r'))
    return info_data