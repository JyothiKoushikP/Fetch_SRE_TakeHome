"""
test_yaml_file_input
Unit tests to check for valid yaml input, invalid yaml files, processing of http requests
This Unit tests comprehensively covers all test case scenarios.
"""

from unittest.mock import patch, mock_open
from ParseYamlInput import loadYamlInput, convertToHttpRequests
from HttpRequest import HttpRequest

'''
Test to check for valid YAML input
'''
def test_load_yaml_input_success():
    mock_yaml_content = """
    name: Test Request
    url: http://example.com
    method: GET
    headers:
      Content-Type: application/json
    body: body content
    """
    with patch("builtins.open", mock_open(read_data=mock_yaml_content)):
        data = loadYamlInput("fake_path.yaml")
        assert data["name"] == "Test Request"
        assert data["url"] == "http://example.com"

'''
Test to check if YAML input file is not found
'''
def test_load_yaml_input_file_not_found():
    with patch("builtins.open", side_effect=FileNotFoundError):
        data = loadYamlInput("fake_path.yaml")
        assert data is None

'''
Test to check if YAML input is converted to Http Requests
'''
def test_convert_to_http_requests():
    request_data = {
        'name': 'Test Request',
        'url': 'http://example.com',
        'method': 'GET',
        'headers': {'Content-Type': 'application/json'},
        'body': 'body content'
    }
    http_request = convertToHttpRequests(request_data)
    assert isinstance(http_request, HttpRequest)
    assert http_request.get_name() == 'Test Request'
    assert http_request.get_url() == 'http://example.com'

