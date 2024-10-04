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

'''
A Template to Process, Store and Calculate the Availability of each Domain per Test Cycle
Keeps Track of all Successful (UP) Requests and Calculates the Availability at the end of each Test Cycle
'''
class AvailabilityTracker:
    def __init__(self):
        self.availability_counts = {}
        self.total_requests = {}

    '''
    Update the Availability Dictionaries after a request is processed by storing it's domain name and request Status (UP/DOWN)
    '''
    def update_availability(self, url, is_up):
        if url not in self.availability_counts:
            self.availability_counts[url] = 0
            self.total_requests[url] = 0

        if is_up:
            self.availability_counts[url] += 1
        self.total_requests[url] += 1

    '''
    Calculates the Availability for each Test Cycle on basis of the stored request status and total requests per domain
    '''
    def calculate_availability(self):
        availability_percentages = {}
        for url in self.availability_counts:
            if self.total_requests[url] > 0:
                availability_percentages[url] = (self.availability_counts[url] / self.total_requests[url]) * 100
            else:
                availability_percentages[url] = 0

        return availability_percentages
