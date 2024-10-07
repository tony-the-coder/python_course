# The delay this time was that I was trying to .strip() first instead of from within the list

# def txt_to_list(file_path):
#     '''Looping through the file to strip the newline character from each line and then returning the list of lines.'''
#     with open (file_path) as f:

#         words = f.readlines()
#         words = [word.strip() for word in words]
#     return words


# You may alter the code below to view your return value(s).
# Only the txt_to_list function will be graded for this assessment.

# print(txt_to_list("text-files/log.txt"))
# Expected return: ['2024-01-28 10:15:32 - User login successful', '2024-01-28 11:20:45 - Firewall rule updated', '2024-01-28 12:35:17 - Network switch rebooted', '2024-01-28 13:40:22 - Server backup started', '2024-01-28 14:55:11 - VPN configuration changed', '2024-01-28 15:10:39 - Intrusion detection system alerted', '2024-01-28 16:25:04 - Software update applied to routers']


import ipaddress


# help(ipaddress)
def get_ip_version(ip_address_str):
    ip = ipaddress(ip_address_str)
    version = ip.version
    return ip, version


# You may alter the code below to view your return value(s).
# Only the get_ip_version function will be graded for this assessment.

# Example usage: "192.168.1.1 is version 4"
results = get_ip_version("192.168.1.1")
print(f"{results[0]} is version {results[1]}")

# Example usage: "2001:db8:85a3::8a2e:370:7334 is version 6"
# results = get_ip_version("2001:0db8:85a3:0000:0000:8a2e:0370:7334")
# print(f"{results[0]} is version {results[1]}")

# help(ipaddress.ip_address)
