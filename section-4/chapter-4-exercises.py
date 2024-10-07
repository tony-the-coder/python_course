"""I am just to toss everything in here since it take a while for the scoring to check if I am right. I figure I can test it in here, and then copy it over to be graded. I just want to save some time for anything that is more than just a few print statements. """

"""Tasks are being thrown into a function to limit the number of comments I have in here."""


def mod_strings():
    """The existing variable "message" collects user input representing a chosen phrase.

    Use built-in methods for string manipulation to print out the user message with the first four characters uppercase and the rest of the message lowercase.
    """

    message = input("Enter a phrase: ")
    # do not edit above this line

    words = message[:4].upper() + message[4:].lower()
    print(words)

    # Expected output for "Modern Networking"
    # MODErn networking


# mod_strings()
