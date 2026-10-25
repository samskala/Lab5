# *******************************************************************************
# Author:          Sam M
# Assignment:      lab5
# Date:            10/24/2026
# Description:     Prompts the user to create a list of movies
# Input:           Movies
# Output:          Outputs selection menu, Editable items, terminal display of
#                  full list on exit, human response to invalid input
# Sources: Python textbook Murach 3rd ed and class material
# *******************************************************************************
from os import get_terminal_size
from menu import display_list, display_banner

# Initialize an empty list to store movie
movies = []

# Show the list of movies
def display_movies(title):
    try:
        width, height = get_terminal_size()
    except:
        width, height = 80, 24
    banner_height = display_banner(title, width, show_datetime=False)
    display_list(movies, width, height, banner_height, center_lines=False)

# Add a movie to the list
def add_movie():
    run = "y"
    while run.lower() == "y":
        display_movies("Add a Movie")
        # Prompt the user to enter a movie
        movie = input("Enter movie title: ")
        # Add the movie to the list
        movies.append(movie)
        print("Movie title added successfully.")
        run = input("Add another? (y/n): ")

# Edit a movie in the list
def edit_movie():
    run = "y"
    while run.lower() == "y":
        # Check if there are movies available to edit
        if movies:
            display_movies("Edit a Movie")
            # Prompt the user to enter the index of the movie to edit
            while True:
                try:
                    movie_index = int(input("Enter movie index to edit: ")) - 1
                    # Check if the entered index is valid
                    if 0 <= movie_index < len(movies):
                        # Prompt the user to enter a new movie
                        new_movie = input("Enter a new movie: ")
                        # Update the movie at the specified index
                        movies[movie_index] = new_movie
                        print("Movie edited successfully.")
                        break
                    else:
                        print("Invalid index.")
                except ValueError:
                    print("Please enter a valid number.")
        else:
            input("No movies available to edit. Press enter to continue...")
            break
        run = input("Edit another? (y/n): ")

# Delete a movie from the list
def delete_movie():
    run = "y"
    while run.lower() == "y":
        # Check if there are movie available to delete
        if movies:
            display_movies("Delete a Movie")
            # Prompt the user to enter the index of the movie to delete
            while True:
                try:
                    movie_index = int(input("Enter movie index to delete: ")) - 1
                    # Check if the entered index is valid
                    if 0 <= movie_index < len(movies):
                        # Remove the movie at the specified index
                        movies.pop(movie_index)
                        print("Movie deleted successfully.")
                        break
                    else:
                        print("Invalid index.")
                except ValueError:
                    print("Please enter a valid number.")
        else:
            input("No movies available to delete. Press enter to continue...")
            break
        run = input("Delete another? (y/n): ")

def exit_movie():
        run = "y"
        while run.lower() == "y":
            if movies:
                print(movies)
            else:
                print("Exiting the application. Goodbye!")
            break
