def identify_high_cpu(cpu_list):
    """If I ever do this again, do not forget to get the actual index number and you need the len to do it not just range"""
    print([cpu for cpu in cpu_list if cpu >= 90])
    return [cpu for cpu in range(len(cpu_list)) if cpu_list[cpu] >= 90]


# You may alter the code below to test your solution or print help documentation.
# Only the identify_high_cpu function will be graded for this assessment.

cpu_list = [85.0, 92.5, 88.0, 95.2]
print(identify_high_cpu(cpu_list))
# help(help)
