# Solution 1: Basic Approach Using a While Loop and List Operations

# Initialize an empty list to store movie
movies = []


# Function to display the available options
def display_menu():
    print("\n1. Add Movie")
    print("2. Edit Movie")
    print("3. Delete Movie")
    print("4. Exit")


# Start an infinite loop to continuously interact with the user
while True:
    # Display the menu options
    display_menu()

    # Get the user's choice
    choice = input("Select an option: ")

    # Option 1: Add movie
    if choice == '1':
        # Prompt the user to enter a movie
        movie = input("Enter movie title: ")
        # Add the movie to the list
        movies.append(movie)
        print("Movie title added successfully.")

    # Option 2: Edit movie
    elif choice == '2':
        # Check if there are movies available to edit
        if movies:
            # Display the current movie with their indices
            for index, movie in enumerate(movies):
                print(f"{index + 1}. {movie}")
            # Prompt the user to enter the index of the movie to edit
            try:
                movie_index = int(input("Enter movie index to edit: ")) - 1
                # Check if the entered index is valid
                if 0 <= movie_index < len(movie):
                    # Prompt the user to enter a new movie
                    new_movie = input("Enter a new movie: ")
                    # Update the movie at the specified index
                    movies[movie_index] = new_movie
                    print("Movie edited successfully.")
                else:
                    print("Invalid index.")
            except ValueError:
                print("Please enter a valid number.")
        else:
            print("No movies available to edit.")

    # Option 3: Delete movie
    elif choice == '3':
        # Check if there are movie available to delete
        if movie:
            # Display the current movie with their indices
            for index, movie in enumerate(movies):
                print(f"{index + 1}. {movie}")
            # Prompt the user to enter the index of the movie to delete
            try:
                movie_index = int(input("Enter movie index to delete: ")) - 1
                # Check if the entered index is valid
                if 0 <= movie_index < len(movies):
                    # Remove the movie at the specified index
                    movies.pop(movie_index)
                    print("Movie deleted successfully.")
                else:
                    print("Invalid index.")
            except ValueError:
                print("Please enter a valid number.")
        else:
            print("No movies available to delete.")

    # Option 4: Exit
    elif choice == '4':
        # Exit the application
        print("Exiting the application. Goodbye!")
        for index, movie in enumerate(movies):
            print(f"{index + 1}. {movie}")
        break

    # Handle invalid menu choices
    else:
        print("Invalid choice. Please select a valid option.")

