"""I need to remember that a single word can change what I am supposed to do. I did not notice that the instructions said set, and I kept getting it wrong. I need to not assume what the instructions are and only do what has been taught so far instead of using what I want!"""

# def generate_users(username_string, num_accounts):
#   '''This is part of the actual question. I did not want to put the whole question in here. While there is a low possibility, I would like to reduce the chance of anyone using my answer instead of learning'''
#   # returning the usernames as a ***set*** to preserve uniqueness.
#   return {username_string + str(num_accounts) for num_accounts in range (1, num_accounts + 1)}

# # You may alter the code below to view your return value(s).
# # Only the generate_users function will be graded for this assessment.

# print(generate_users("test_account", 4))


# def remove_admin(usernames, limit):
#     '''I read it, but the question did not seem very clear. '''
#     i = 0
#     validated = []
#     admin_count = 0

#     while i < limit:
#         if "admin" in usernames[i]:
#             admin_count += 1
#         else:
#             validated.append(usernames[i])
#         i += 1
#     validated.append("validated")

# remove "admin" usernames based on limit
# return validated list with appended "validated" entry
# return count of removed admin usernames

# return validated, admin_count


# You may alter the code below to view your return value(s).
# Only the generate_users function will be graded for this assessment.

# usernames = [
#     "FN84",
#     "adminPD66",
#     "OP83",
#     "IT32",
#     "OP27",
#     "OP13",
#     "IT95",
#     "adminHR73",
#     "OP12",
#     "HR31",
# ]
# print(remove_admin(usernames, 10))

# Expected return
# (['FN84', 'OP83', 'IT32', 'OP27', 'OP13', 'IT95', 'OP12', 'HR31', 'validated'], 2)


def department_count(entries):
    """Another not so clear question. I should have assumed what it wanted from the tests that did not pass. In this case, I should have checked to make sure that the count was was in entries. I actually has to use GitHub Copilot to help. I have to get better since I am sure I cannot use AI to help me catch such a simple mistake as missing that if statement."""

    department_codes = ["HRD", "ENG", "MKT", "FIN", "IT"]
    department_counts = {count: 0 for count in department_codes if count in entries}
    invalid_count = 0

    for entry in entries:
        if entry in department_codes:
            department_counts[entry] += 1

        elif entry not in department_codes and entry != "TEST":
            invalid_count += 1

    # count entries per department
    # return department_counts dictionary
    # return invalid_count, excluding "TEST" values

    return department_counts, invalid_count


# You may alter the code below to view your return value(s).
# Only the generate_users function will be graded for this assessment.

entries = [
    "HRD",
    "MKT",
    "HRD",
    "IT",
    "ENG",
    "HRD",
    "TEST",
    "HRD",
    "TEST",
    "HRD",
    "HRD",
    "TEST",
    "IT",
    "TEST",
    "HRD",
    "TEST",
    "IT",
    "TEST",
    "ENG",
    "MKT",
    "TEST",
    "IT",
    "IT",
    "HRD" "GUEST",
]
print(department_count(entries))

# Expected return
# ({'HRD': 7, 'MKT': 2, 'IT': 5, 'ENG': 2}, 1)
