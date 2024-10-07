def validate_id(emp_id):
    """Instrunctions were okay, but still not the best."""
    test_users = emp_id[0:3]
    if test_users.isalpha and test_users == test_users.upper() and len(emp_id) == 8:
        return True
    return False


# You may alter the code below to test your solution or print help documentation.
# Only the validate_id function will be graded for this assessment.

print(validate_id("IT12345"))
# help(help)
