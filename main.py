import datetime
import re

# Pattern for extraction datetime string from squate brackets
pattern_for_datetime_extraction = r'\[.*\]'

# Datetime format for datetime object manipulation
datetime_format = "[%Y-%m-%d %H:%M:%S]"

# Read file as Python's list of lines
with open("events.log", "r") as log_file:
    list_of_lines = log_file.readlines()

# Get the first and the last timestamps to make datetime range between them
first_timestamp = re.search(pattern_for_datetime_extraction, list_of_lines[0]).group(0)
first_timestamp = datetime.datetime.strptime(first_timestamp, datetime_format)
last_timestamp = re.search(pattern_for_datetime_extraction, list_of_lines[-1]).group(0)
last_timestamp = datetime.datetime.strptime(last_timestamp, datetime_format)

# Create initial dict with minutes as keys and zeroes as values for further NOK counting
dict_of_nok_counts = dict()
delta = last_timestamp - first_timestamp
for i in range(0, delta.seconds + 60, 60):
    minute = first_timestamp + datetime.timedelta(seconds=i)
    minute = minute.replace(second=0)
    dict_of_nok_counts[minute] = 0

# Searching through the list of lines for NOK's and incrementing the dict count
for line in list_of_lines:
    if "NOK" in line:
        timestamp = re.search(pattern_for_datetime_extraction, line).group(0)
        timestamp = datetime.datetime.strptime(timestamp, datetime_format)
        timestamp = timestamp.replace(second=0)
        dict_of_nok_counts[timestamp] += 1

for key, value in dict_of_nok_counts.items():
    print(key, value)
