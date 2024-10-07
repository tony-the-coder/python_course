# Modify this function.
def line_count(filename):
    with open(filename) as f:
        x = f.readlines()
        x = len(x)
    return x


# You may alter the code below to test your solution or print help documentation.
# Only the line_count function will be graded for this assessment.

print(line_count("practice_lab_files\test.txt"))


# help(help)
