def update_log_list(log_list):
    # Write your code here.

    """Trying to stay within bounds of what was taught"""
    for log in log_list:
        if log["app"] == "webserver":
            log["level"] = "ERROR"
        if log["app"] == "database":
            log["timestamp"] = "2023-12-07T12:30:00"
    return log_list

    # for log in log_list:
    #     if log["app"] == "webserver":
    #         log["level"] = "ERROR"
    #     if log["app"] == "database":
    #         log["timestamp"] == "2023-12-07T12:30:00"
    # return log_list


# You may alter the code below to test your solution or print help documentation.
# Only the update_log_list function will be graded for this assessment.

log_sample = [
    {
        "app": "webserver",
        "level": "w",
        "message": "Critical error",
        "timestamp": "2023-12-07T11:55:00",
    },
    {
        "app": "database",
        "level": "ERROR",
        "message": "Database connection lost",
        "timestamp": "2023-12-07T11:50:00",
    },
]
print(update_log_list(log_sample))
# help(help)
