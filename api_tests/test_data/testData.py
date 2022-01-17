import os
import json


def readJson(jsonFilePath):
    with open(jsonFilePath) as f:
        jsonFile = json.load(f)

    return jsonFile


def get_value(attribute_name):
    testDataPath = os.path.abspath("api_tests/test_data/API_test_data.json")
    testDataJsonFile = readJson(testDataPath)
    return testDataJsonFile[attribute_name]

