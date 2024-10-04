"""
ParseYamlInput.py
This file consists of the modular functions required to take the input YAML file
and parse them into HttpRequests Objects.
Robust Exception Handling is done to handle invalid file paths, invalid yaml inputs

LoadYamlInput
Takes the YAML File Path and parses the file and collects the YAML Input

ConvertToHttpRequests
Takes the YAML Input from LoadYamlInput and converts it to HttpRequests Objects
"""


import yaml
from HttpRequest import HttpRequest

'''
Loads the YAML Input file and Stores entry HttpRequest Entry in a Dictionary
Output is a list of Dictionaries with Keys (Header, Name, URL, Method, Body) -> YAML Key Metadata
'''
def loadYamlInput(filepath):
    http_requests_data = None
    try:
        with open(filepath) as f:
            http_requests_data = (yaml.safe_load(f))
    except FileNotFoundError:
        print(f"File not Found....")
    except yaml.YAMLError as exc:
        print(f"Error: an issue occurred...parsing the file")
    except Exception as e:
        print(f"An unexpected error")

    return http_requests_data

'''
Converts the YAML Input to a HttpRequest Object for re-usability, modularity and easier processing
For The Template Structure refer to HttpRequests.py
'''
def convertToHttpRequests(requestData):
    name = requestData.get('name')
    url = requestData.get('url')
    method = requestData.get('method')
    headers = requestData.get('headers')
    body = requestData.get('body')
    return HttpRequest(name, url, method, headers, body)

