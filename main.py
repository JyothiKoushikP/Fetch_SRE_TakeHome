"""
main.py -> Main Entrypoint for the assignment
The program execution starts from this point
The Main Block keeps on running the Test Cycle every 15 seconds until the User Exits with
Ctrl + C termination which is caught by the Signal Handler Function (SIGINT)

The Test Cycle outputs the test results every 15 seconds
When the user exits the program, the code logs the final running test cycle
"""

import os
import time
import sys
from Logger import log_final_availability
from ParseYamlInput import loadYamlInput, convertToHttpRequests
from HttpChecker import check_http_requests
from AvailabilityTracker import AvailabilityTracker
import signal

'''
Handles SIGINT handler to exit the program on Keyboard Interrupt (Ctrl + C)
This is injected into the main function to watch and exit the program on Keyboard Interrupt
'''
def signal_handler(sig, frame):
    print("Exiting... Logging final availability.")
    log_final_availability(tracker)  # Log before exit
    sys.exit(0)

'''
Entrypoint for the whole project
Uses all the other Classes, Modules and Functions to run the test cycle for every 15 seconds and outputs the availability of each domain
UP: (Status code: 200 - 299 and Latency < 500ms)
Based on this, the program runs till the user stops the execution by pressing Ctrl + C
Loads the YAML Input based on the INPUT_FILE ENV Variable (By Default or provided by User)
'''
if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    # Load YAML input (ParseYamlInput.py)
    filepath = os.getenv('INPUT_FILE')
    request_data = loadYamlInput(filepath)
    # Checking for Request Data and converting it to HttpRequests Objects (HttpRequests.py)
    if request_data:
        http_requests = [convertToHttpRequests(data) for data in request_data]

        # Availability Tracker Object to keep Track of Cycles (AvailabilityTracker.py)
        tracker = AvailabilityTracker()
        try:
            # Executing Continuous Test Cycles and Logging for every Test Cycle (Handling Exceptions)
            time_p = 0
            while True:
                print(f"Test cycle #{(time_p//15) + 1} begins at time = {time_p} seconds:")
                check_http_requests(http_requests, tracker)
                time.sleep(15)
                log_final_availability(tracker)
                time_p += 15
        except Exception as e:
            # Exception Handling
            print(f"An Error occurred: {e}")
