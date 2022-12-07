# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from yaml import full_load
from utilities import utilities

def main():
    with open('config.yml') as file:
        conf = full_load(file)
    utility = utilities(conf)
    data = """
    Thank you for attending todays interview for the above role.

    The hiring manager has asked if you can please complete a coding exercise?  Based on this, we will then decide on how to proceed with your application.

    The exercise is this:

    You are to implement a function in the language of your choice which reads some text and counts how often words occur.  
    This is to be your own original work, where the algorithm is the most important component.  You may make your own design choices where there is ambiguity.
    """
    utility.parse_string(data)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
