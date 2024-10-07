from datetime import datetime


def find_latest(submissions):
    # Specify a date format
    date_format = "%m/%d/%Y %I:%M %p"

    # Convert string values into datetime objects.
    # x = [time.datetime(date_format) for time in submissions]
    # print(x)

    # for time in submissions:
    # y = [datetime.strptime(time, date_format) for time in submissions]

    # return max(y)

    # Determine and return latest
    return max(datetime.strptime(time, date_format) for time in submissions)


# You may alter the code below to test your solution or print help documentation.
# Only the find_latest function will be graded for this assessment.

submission_timestamps = [
    "12/15/2023 08:45 AM",
    "12/14/2023 03:30 PM",
    "12/16/2023 11:20 AM",
    "12/13/2023 06:15 PM",
]
print(find_latest(submission_timestamps))
# help(datetime.strptime)
