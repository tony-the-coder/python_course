import socket
import time
import unittest.mock as mock


def scan_ports(x):
    # Mock socket
    with mock.patch("socket.socket") as mock_socket:
        mock_socket.return_value.connect_ex.return_value = 0  # do not edit
        target_IP = "127.0.0.1"

        # Instantiate a socket object.
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Set a timeout for the socket operations.
        s.settimeout(5)

        # Create an empty list to store port status as a list tuples.
        open_ports = []

        # Iterate over ports checking the connection and appending the port status to the list.
        for i in range(0, x + 1):
            conn = s.connect_ex((target_IP, i))
            if conn == 0:
                open_ports.append((i, "OPEN"))
            else:
                open_ports.append((i, "CLOSED"))

        # Close the socket connection.
        s.close()

        # Return the list of open ports as a list of tuples.
        return open_ports


# You may alter the code below to test your solution or print help documentation.
# Only the scan_ports function will be graded for this assessment.

print(scan_ports(5))
# help(socket.socket)
# help(socket.socket.connect_ex)
