"""
test_check_httprequest.py
A pytest module that tests the HttpRequest Objects on various case-scenarios
Invalid / Empty Name
Invalid / Empty URL
Optional Headers, Body
Optional Method = "GET
"""

import pytest
from HttpRequest import HttpRequest

'''
Test for Valid HttpRequest with all fields
'''
def test_http_request_initialization_valid():
    request = HttpRequest("Test Request", "http://example.com", "GET", {"Content-Type": "application/json"},
                          "body content")

    assert request.get_name() == "Test Request"
    assert request.get_url() == "http://example.com"
    assert request.get_method() == "GET"
    assert request.get_headers() == {"Content-Type": "application/json"}
    assert request.get_body() == "body content"

'''
Test for None "Name" Object
'''
def test_http_request_set_name_invalid_none():
    with pytest.raises(ValueError, match="The 'name' cannot be None."):
        HttpRequest(None, "http://example.com", "GET", {}, "body content")

'''
Test for Empty "Name" Object
'''
def test_http_request_set_name_invalid_empty():
    with pytest.raises(ValueError, match="The 'name' cannot be None."):
        HttpRequest("", "http://example.com", "GET", {}, "body content")

'''
Test for None "URL" Object
'''
def test_http_request_set_url_invalid_none():
    with pytest.raises(ValueError, match="The 'url' cannot be None."):
        HttpRequest("Test Request", None, "GET", {}, "body content")

'''
Test for Empty "Name" Object
'''
def test_http_request_set_url_invalid_empty():
    with pytest.raises(ValueError, match="The 'url' cannot be None."):
        HttpRequest("Test Request", "", "GET", {}, "body content")

'''
Test for Default Method = "GET"
'''
def test_http_request_set_method_default():
    request = HttpRequest("Test Request", "http://example.com", None, {}, "body content")
    assert request.get_method() == "GET"

'''
Test for Default Headers = {}
'''
def test_http_request_set_headers_default():
    request = HttpRequest("Test Request", "http://example.com", "GET", None, "body content")
    assert request.get_headers() == {}

'''
Test for Default Body = ""
'''
def test_http_request_set_body_default():
    request = HttpRequest("Test Request", "http://example.com", "GET", {}, None)
    assert request.get_body() == ""
