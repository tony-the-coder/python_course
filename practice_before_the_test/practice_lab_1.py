def format_rgb(rgb):
    """The instructions were not asking for the rgb to be returned as a tuple, I was overthinking it. I should have just returned the string. I need to remember that the instructions are not always asking for the same thing. I need to make sure that I am reading the instructions and not assuming what they are asking for."""
    return f"rgb({','.join(str(x) for x in rgb)})"


# You may alter the code below to test your solution or print help documentation.
# Only the format_rgb function will be graded for this assessment.

rgb_sample = [255, 165, 13]
print(format_rgb(rgb_sample))
# help(help)
