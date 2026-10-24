#*****************************************************************************
# Author:          Josh Meyer
# Lab:             CIS-133Y Lab5
# Date:            10/23/2026
# Description:     Functions for displaying clean menu options
# Input:           string: selected, integer: selected
# Output:          Top of screen banner and a dynamic menu for displaying
#                  each available option.
# Sources:         
#*****************************************************************************
from datetime import datetime


OPTIONS = [
    #{"name":"Add Numbers","app":addition},
    #{"name":"Subtract Numbers","app":subtraction},
    #{"name":"Multiply Numbers","app":multiplication},
    #{"name":"Divide Numbers","app":division},
]


# Formats a string with whitespace on either side of it to size of the
# width minus 2. Example:
#"                                   Title                                   "
# - Josh Meyer
def center_format_string(width, string):
    # Determine the size of whitespace needed on each side
    whitespace = (width - len(string))//2 - 1
    # Generate the formatted string
    display_string = "{spacing}{naming}{spacing}".format(spacing = \
        (" " * whitespace), naming = string)
    # If there is an odd number of characters in the display string, add
    # an extra space to the end
    if len(display_string) != (width - 2):
        display_string += " "
    return display_string


# Formats a string with whitespace on the right side, to left justify the
# the string to the size of the width minus 4. Example:
#"1) Function One                                                          "
# - Josh Meyer
def display_left_formatted_string(width, string):
    # Calculate the remaining white space
    whitespace = (width - len(string) - 4)
    # Display the formatted
    print("* {string}{whitespace} *".format(string = string,\
        whitespace = (" " * whitespace)))


# Display a menu with padding from the top to fill the screen. Example:
# ... extra lines omitted ...
#* 1) Item One                                                               *
#* 2) Item Two                                                               *
#* 3) Item Three                                                             *
#*****************************************************************************
# - Josh Meyer
def display_list(options, width, height, banner = 0, fill_screen = True):
    if fill_screen:
        # If fill the screen is selected determine the number of extra lines
        #  needed, subtracting an extra 2 for the bottom border and
        #  input request
        whitelines = height - len(options) - banner - 2

        for i in range(0, whitelines):
            # For each extra line, print a bordered blank line
            print("*{spacing}*".format(spacing = (" " * (width - 2))))

    for i in range(0, len(options)):
        # Set the number for selection and the name of the function
        display_left_formatted_string(width,"{num}) {name}".format(\
            num = i + 1, name = options[i]["name"]))
        
    # Print the bottom border
    print("*" * (width))


# Detemine the break point for a string to fit within the desired confines
# -Josh Meyer
def break_text(fulltext, width):
    # Initialize which characters to attempt a break on
    break_point = " "
    breaks = [" ","-","_",".","/","\\","|"]
    for point in breaks:
        # If the type of break_point exists in the full text, set the variable
        #  and break from the loop
        if fulltext.count(point) > 0:
            break_point = point
            break
    # Get the last index of the break_point to create substrings
    index = fulltext[0:width].rindex(break_point)
    # return the first chunk
    return fulltext[0:index + 1]
        

# Display a top banner with the title and optional datetime stamp. Example:
#*****************************************************************************
#*                              Title                                        *
#*                     2026-10-13 20:50:19 PM                                *
#*****************************************************************************
# - Josh Meyer
def display_banner(title, width, show_datetime = True, center_lines = True):
    # Initialize variables
    count = 3 # Includes top and bottom border with 1 line for title
    max_title_width = (width - 4)
    # Print top border
    print("*" * (width))
    # Determine if title is larger than width and break it into sections
    #  before truncating the rest
    while len(title) > max_title_width:
        subtext = break_text(title, max_title_width)
        if center_lines:
            # Print "*" on either side of the subtext while centering it
            #  with whitespace.
            display_string = center_format_string(width, subtext)
        else:
            # Print "*" on either side of the subtext while left adjusting it
            #  with whitespace.
            display_string = display_left_formatted_string(width, subtext)
        print("*{string}*".format(string = display_string))
        # Update the title variable to remove already displayed portions
        title = title[len(subtext):]
        # Add to count
        count += 1
 
    if center_lines:
        # Print "*" on either side of the title while centering it
        #  with whitespace.
        display_string = center_format_string(width, title)
    else:
        # Print "*" on either side of the title while left adjusting it
        #  with whitespace.
        display_string = display_left_formatted_string(width, title)
    print("*{string}*".format(string = display_string))

    if show_datetime:
        # Get the current date and time
        current_time = datetime.now()
        # Format current_time to this style: 2026-10-01 12:10:05 PM
        current_time_string = str(current_time.date()) + \
            " " + str(current_time.strftime("%H:%M:%S %p"))
        # Print "*" on either side of the datetime stamp while centering it
        #  with whitespace.
        display_string = center_format_string(width, current_time_string)
        print("*{string}*".format(string = display_string))
        # Add to count
        count += 1

    # Print bottom border
    print("*" * (width))
    # Return the number of lines displayed
    return count
