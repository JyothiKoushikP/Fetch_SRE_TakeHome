"""
Logger.py
Python file for Logging Availability (UP/DOWN) at the end of each test cycle
Takes the Availability Tracker function and Outputs the total rounded availability percentage
of the Test Cycle
"""

'''
Logs the Availability Percentage per Domain at the End of Each Test Cycle (Cumulative)
Rounded to the Nearest Integer on the Scale of 100
'''
def log_final_availability(tracker):
    availability = tracker.calculate_availability()
    for url, percentage in availability.items():
        print(f"{url} has {round(percentage)}% availability percentage")
    print("###################################################")
