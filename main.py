# *******************************************************************************
# Author:          Sam M, Josh Meyer
# Assignment:      lab5
# Date:            10/24/2026
# Description:     Prompts the user to create a list of movies
# Input:           Menu Selection
# Output:          Outputs selection menu, Editable items, terminal display of
#                  full list on exit, human response to invalid input
# Sources: Python textbook Murach 3rd ed and class material
# *******************************************************************************
from os import get_terminal_size
from menu import display_list, display_banner
from movies import add_movie, edit_movie, delete_movie

# Menu Options; the name of the function to display and the app executable
MENU_OPTIONS = [
    {"name":"Add Movie","app": add_movie},
    {"name":"Edit Movie","app": edit_movie},
    {"name":"Delete Movie","app": delete_movie},
    {"name":"Exit"} # Always last
]


def main():
    # Start a loop to continuously interact with the user
    choice = 0
    while choice != str(len(MENU_OPTIONS)):
        # Get size of the terminal window
        try:
            width, height = get_terminal_size()
        except:
            width, height = 80, 24
        # Display the menu options
        banner_height = display_banner("Let's create a favorite movie list!",
            width, show_datetime=False)
        display_list(MENU_OPTIONS, width, height, banner_height, center_lines=False)

        # Get the user's choice
        choice = input("Select an option: ")
        # Validate input is a digit
        if str.isdigit(choice):
            # Validate the digit falls within the number of options
            if int(choice) > 0 and int(choice) < len(MENU_OPTIONS):
                # From the MENU_OPTIONS array, get the selected index. Get the
                #  value from the "app" key, which is an imported function.
                #  With the parentheses added to the function, it executes.
                MENU_OPTIONS[int(choice) - 1]["app"]()
        print("")
       
main()