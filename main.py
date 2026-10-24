# *******************************************************************************
# Author:          Sam M, Josh Meyer
# Assignment:      lab5
# Date:            10/23/2026
# Description:     Prompts the user to create a list of movies
# Input:           Movies
# Output:          Outputs selection menu, Editable items, terminal display of
#                  full list on exit, human response to invalid input
# Sources: Python textbook Murach 3rd ed and class material
# *******************************************************************************
from os import get_terminal_size
from menu import display_list, display_banner
# from movie_func import add_movie, edit_movie

# Example definition that would be imported
# Initialize an empty list to store movie
movies = []

def add_movie():
    run = "y"
    while run.lower() == "y":
        width, height = get_terminal_size()
        banner_height = display_banner("Add a Movie", width, show_datetime=False)
        display_list(movies, width, height, banner_height, center_lines=False)
        # Prompt the user to enter a movie
        movie = input("Enter movie title: ")
        # Add the movie to the list
        movies.append(movie)
        print("Movie title added successfully.")
        run = input("Add another? (y/N): ")

# Menu Options; the name of the function to display and the app executable
MENU_OPTIONS = [
    {"name":"Add Movie","app": add_movie},
    {"name":"Edit Movie"},#,"app": edit_movie},
    {"name":"Delete Movie"},#,"app": delete_movie},
    {"name":"Exit"} # Always last
]


def main():
    # Start a loop to continuously interact with the user
    choice = 0
    while choice != str(len(MENU_OPTIONS)):
        # Get size of the terminal window
        width, height = get_terminal_size()
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


    # Option 2: Edit movie
#    elif choice == '2':
        # Check if there are movies available to edit
#        if movies:
            # Display the current movie with their indices
#            for index, movie in enumerate(movies):
#                print(f"{index + 1}. {movie}")
            # Prompt the user to enter the index of the movie to edit
#            try:
#                movie_index = int(input("Enter movie index to edit: ")) - 1
                # Check if the entered index is valid
#                if 0 <= movie_index < len(movie):
                    # Prompt the user to enter a new movie
#                    new_movie = input("Enter a new movie: ")
                    # Update the movie at the specified index
#                    movies[movie_index] = new_movie
#                    print("Movie edited successfully.")
#                else:
#                    print("Invalid index.")
#            except ValueError:
#                print("Please enter a valid number.")
#        else:
#            print("No movies available to edit.")

    # Option 3: Delete movie
#    elif choice == '3':
        # Check if there are movie available to delete
#        if movie:
            # Display the current movie with their indices
#            for index, movie in enumerate(movies):
#                print(f"{index + 1}. {movie}")
            # Prompt the user to enter the index of the movie to delete
#            try:
#                movie_index = int(input("Enter movie index to delete: ")) - 1
                # Check if the entered index is valid
#                if 0 <= movie_index < len(movies):
                    # Remove the movie at the specified index
#                    movies.pop(movie_index)
#                    print("Movie deleted successfully.")
#                else:
#                    print("Invalid index.")
#            except ValueError:
#                print("Please enter a valid number.")
#        else:
#            print("No movies available to delete.")

    # Option 4: Exit
#    elif choice == '4':
        # Exit the application
#        print("Exiting the application. Goodbye!")
#        for index, movie in enumerate(movies):
#            print(f"{index + 1}. {movie}")
#        break

    # Handle invalid menu choices
#    else:
#        print("Invalid choice. Please select a valid option.")

