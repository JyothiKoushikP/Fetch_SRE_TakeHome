"""
AvailabilityTracker.py

This file consists of the AvailabilityTracker Class which is responsible for maintain
the availability percentage per domain for all test Cycles

We use a Dictionary Data Structure to keep track of unique domains and their occurences

For Every Test Cycle:
Depending on the Status: UP/DOWN
The availability_counts keeps track of unique domain and their count (UP)
The total_requests keeps track of all the requests that have occured till time per domain.

Based on these data:
Availability Percentage for a domain is calculated:

(Total number of UPS / Total Requests) * 100
"""

import requests
import tldextract

'''
Processes all the HttpRequests Objects by sending requests, calculating the latency and status_code (UP/DOWN)
'''
def check_http_requests(http_requests, tracker):
    for http_request in http_requests:
        try:
            '''
            This Block takes all the HttpRequests objects, extracts the method, url, headers, body and processes the request
            We use tldextract to extract the domain of a url (SubDomain.Domain.Suffix)
            Based on the Response: The Availability Tracker calculates and keeps track of the availability
            Any interrupted requests are handled through the exception block below
            '''
            method = http_request.get_method()
            url = http_request.get_url()
            headers = http_request.get_headers()
            body = http_request.get_body()

            if method == "POST":
                response = requests.post(url, headers=headers, json=body)
            else:
                response = requests.get(url, headers=headers)

            latency = response.elapsed.total_seconds() * 1000
            is_up = response.status_code // 100 == 2 and latency < 500
            domain = extracted_domain(url)

            # Log the availability
            tracker.update_availability(domain, is_up)

        except requests.exceptions.RequestException as e:
            print(f"Request failed for {http_request.get_name()}: {e}")
            tracker.update_availability(http_request.get_url(), False)


'''
Extracts the Domain (SubDomain.Domain.Suffix) From the URL for the Availability Track to keep track
'''
def extracted_domain(url):
    domain = []
    extracted = tldextract.extract(url)
    if extracted.subdomain:
        domain.append(extracted.subdomain)
    if extracted.domain:
        domain.append(extracted.domain)
    if extracted.suffix:
        domain.append(extracted.suffix)

    return ".".join(domain)
