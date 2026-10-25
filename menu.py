#*****************************************************************************
# Author:          Josh Meyer
# Lab:             CIS-133Y Lab5
# Date:            10/24/2026
# Description:     Functions for displaying clean menu options
# Input:           
# Output:          Top of screen banner and a dynamic menu for displaying
#                  each available option.
# Sources:         
#*****************************************************************************
from datetime import datetime

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
def left_formatted_string(width, string):
    # Calculate the remaining white space
    whitespace = (width - len(string) - 4)
    # Display the formatted
    return " {string}{whitespace} ".format(string = string,\
        whitespace = (" " * whitespace))


# Display a menu with padding from the top to fill the screen. Example:
# ... extra lines omitted ...
#* 1) Item One                                                               *
#* 2) Item Two                                                               *
#* 3) Item Three                                                             *
#*****************************************************************************
# - Josh Meyer
def display_list(options, width, height, banner = 0, fill_screen = True,
    center_lines = True):
    if fill_screen:
        # If fill the screen is selected determine the number of extra lines
        #  needed, subtracting an extra 2 for the bottom border and
        #  input request
        whitelines = height - len(options) - banner - 2

        for i in range(0, whitelines):
            # For each extra line, print a bordered blank line
            print("*{spacing}*".format(spacing = (" " * (width - 2))))

    # Initialize max_width with 4 for the '*'s and spaces on both ends and
    #  another 2 for digit and ')' before the text and 1 for safe measure
    max_width = width - 7 
    if len(options) > 9:
        # Getting into double digit numbers, add an extra space of padding
        max_width -= 1
    if len(options) > 99:
        # Why are we crossing into triple digits?
        max_width -= 1

    for i in range(0, len(options)):
        # Initialize
        if type(options[i]) == dict:
            name = options[i]["name"]
        else:
            name = options[i]
        first = True
        # Determine if option name is larger than width and break it into
        #  sections before displaying the rest
        while len(name) > max_width:
            subtext = break_text(name, max_width)
            if first:
                # If this is the first line, display the number for selection
                prepended_text = "{num}) {text}".format(num = i + 1, text = subtext)
            else:
                # Not being the first line, add some extra padding to align
                whitespace = width - (max_width + 4)
                prepended_text = "{whitespace}{text}".format(whitespace = \
                    (" " * whitespace), text = subtext)
            if center_lines:
                # Print "*" on either side of the prepended_text while centering it
                #  with whitespace.
                display_string = center_format_string(width, prepended_text)
            else:
                # Print "*" on either side of the prepended_text while left adjusting
                #  it with whitespace.
                display_string = left_formatted_string(width, prepended_text)
            print("*{string}*".format(string = display_string))
            # Update the name variable to remove already displayed portions
            name = name[len(subtext):]
            first = False
        # Either the name is not longer than the max_width or it has been 
        #  reduced enough to display the last line
        if first:
            # If this is the first line, display the number for selection
            text = "{num}) {text}".format(num = i + 1, text = name)
        else:
            # Not being the first line, add some extra padding to align
            whitespace = width - (max_width + 4)
            text = "{whitespace}{text}".format(whitespace = \
                (" " * whitespace), text = name)
        if center_lines:
            # Print "*" on either side of the subtext while centering it
            #  with whitespace.
            display_string = center_format_string(width, text)
        else:
            # Print "*" on either side of the subtext while left adjusting
            #  it with whitespace.
            display_string = left_formatted_string(width, text)
        print("*{string}*".format(string = display_string))
        
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
    #  before diplaying the rest
    while len(title) > max_title_width:
        subtext = break_text(title, max_title_width)
        if center_lines:
            # Print "*" on either side of the subtext while centering it
            #  with whitespace.
            display_string = center_format_string(width, subtext)
        else:
            # Print "*" on either side of the subtext while left adjusting it
            #  with whitespace.
            display_string = left_formatted_string(width, subtext)
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
        display_string = left_formatted_string(width, title)
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
