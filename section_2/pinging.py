import os

"""Random code example for pinging a server that did not work from the 'book' but it is probably because I am on Windows right now"""


def ping_server(ip_address):
    device_status = {}

    for ip in ip_address:
        response = os.system(f"ping -n 1 {ip}")
        if response == 0:
            device_status[ip] = "Active"
        else:
            device_status[ip] = "Inactive"

    return device_status


ping_server(["8.8.8.8"])
