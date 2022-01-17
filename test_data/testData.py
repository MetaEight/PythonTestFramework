import os
import json


def readJson(jsonFilePath):
    with open(jsonFilePath) as f:
        jsonFile = json.load(f)

    return jsonFile


def get_value(page, attribute_name):
    testDataPath = os.path.abspath("test_data/test_data.json")
    testDataJsonFile = readJson(testDataPath)
    return testDataJsonFile[page][attribute_name]

