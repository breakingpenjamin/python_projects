# Name: Keyshawn Curtis
# Movie Watchlist Program

# This program was designed to display a menu of options that will allow the user
# to interact with several lists in various ways such as editing the list,
# searching the list, and sorting the list ...etc.


# Global Variables - movie lists
MOVIE_LIST_1 = ['Kill Bill', 'The Matrix', 'The Lord of the Rings', 'The Dark Knight', 'Inception', 'The Shawshank Redemption', 'Pulp Fiction', 'The Godfather', 'The Avengers', 'Interstellar', 'Sinners', 'Pirate of the Caribbean']
MOVIE_LIST_2 = []
MOVIE_LIST_3 = []

# DISPLAY program HEADER
def display_header():
    print()
    print('=============================')
    print('     Movie Watchlist App     ')
    print('=============================')

# DISPLAY the MENU of options
def display_menu():
    print()
    print('\nMenu Options:')
    print('----------------------')
    print('1. Display all movies in Watchlist 1 - sorted by Title')
    print('2. Create/add a movie to Watchlist 2')
    print('3. Display all movies in Watchlist 2 - sorted by Title')
    print('4. Merge Watchlist 1 and Watchlist 2 and place into Watchlist 3')
    print('5. Display all movies in Watchlist 3 - sorted by Title')
    print('==========================================================================================================================')
    print('\tALl the remaining selections pertain to the merged Watchlist 3 (the combined Watchlist 1 and Watchlist 2)')
    print('==========================================================================================================================')
    print('6. Display how many movies are in watchlist')
    print('7. Add movie to end of Watchlist')
    print('8. Add movie to beginning of Watchlist')
    print('9. Remove movie from Watchlist')
    print('10. Search for a movie in Watchlist')
    print('11. Display Movies Beginning with "T" in Watchlist')
    print('12. Sort Watchlist in descending order')
    print('13. Display the first 3 movies in Watchlist')
    print('14. Display the last 3 movies in Watchlist')
    print('15. Exit the program')

# DISPLAY ALL movies in watchlist
def display_watchlist(movie): # passing the movie list as an argument
    print('\n==== Movies in Watchlist: ====')
    print('')  
    for index in movie: # index is the variable that will represent each movie in the list as we loop through it
        print(index)
    print('\n================================')

# SORT watchlist in alphabetical ASCENDING order
def sort_watchlist(movie):
    movie.sort()
    print('\nMovies in Watchlist (sorted in ascending order)')

# SORT watchlist in alphabetical DESCENDING order
def sort_watchlist_descending(movie):
    movie.sort(reverse=True)
    print('\nMovies in Watchlist (sorted in descending order)')

# CREATE/ADD a movie to watchlist 2
def create_add_movie_watchlist_2():
    keep_going = 'y'
    while keep_going == 'y': 
        movie_title = input('Enter the title of the movie you want to add to Watchlist 2: ')
        MOVIE_LIST_2.append(movie_title)
        print(f'\n"{movie_title}" has been added to Watchlist 2.')
        add_another = input('\nDo you want to add another movie to Watchlist 2? (y/n): ')
        if add_another == 'n' or add_another == 'N':
            keep_going = 'n'
            print('\nFinished adding movies to Watchlist 2.')

# MERGE watchlist 1 and watchlist 2 and place into watchlist 3
def merge_watchlists(watchlist_1, watchlist_2): # passing the two watchlists as arguments to the merge_watchlists function to merge them into a new watchlist
    watchlist_3 = watchlist_1 + watchlist_2 
    print('\nWatchlist 1 and Watchlist 2 have been merged into Watchlist 3.')
    return watchlist_3 # returning the merged watchlist to be used in the main function when the user selects option 4 to merge the watchlists

# DISPLAY how many movies are in watchlist
def number_of_movies(movie):
    num_movies = len(movie)
    print(f'\nThere are {len(movie)} movies in the Watchlist.')

# ADD movie to end of watchlist
def add_movie_end(movie):
    add_movie_end = input('Enter the title of the movie you want to add to the end of Watchlist: ')
    if add_movie_end in movie:
        print(f'\n"{add_movie_end}" is already in Watchlist. Please enter a different movie title.')
    else:
        movie.append(add_movie_end)
        print(f'\n"{add_movie_end}" has been added to the end of Watchlist.')

# ADD movie to beginning of watchlist
def add_movie_beginning(movie):
    add_movie_beginning = input('\nEnter the title of the movie you want to add to the beginning of Watchlist: ')
    if add_movie_beginning in movie:
        print(f'\n"{add_movie_beginning}" is already in Watchlist. Please enter a different movie title.')
    else:
        movie.insert(0, add_movie_beginning)
        print(f'\n"{add_movie_beginning}" has been added to the beginning of Watchlist.')

# REMOVE movie from watchlist
def remove_movie(movie):
    remove_movie = input('Enter the title of the movie you want to remove from Watchlist: ')
    if remove_movie in movie:
        movie.remove(remove_movie)
        print(f'\n"{remove_movie}" has been removed from Watchlist.')
        display_watchlist(movie) # display the updated watchlist after removing the movie
    else:
        print(f'\n"{remove_movie}" is not in Watchlist.')

# SEARCH for a movie in watchlist
def search_movie(movie):
    search_movie = input('Enter the title of the movie you want to search for in Watchlist: ')
    if search_movie in movie:
        print(f'\n"{search_movie}" is in Watchlist.')
    else:
        print(f'\n"{search_movie}" is not in Watchlist.')

# DISPLAY first 3 movies in watchlist
def display_first_3_movies(movie):
    print('\nThe first 3 movies in Watchlist are:')
    print('')
    for index in range(min(3, len(movie))): # using min function to ensure we don't try to access more movies than are in the list
        print(movie[index])

# DISPLAY last 3 movies in watchlist
def display_last_3_movies(movie):
    print('\nThe last 3 movies in Watchlist are:')
    print('')
    for index in range(max(0, len(movie) - 3), len(movie)): # using max function to ensure we don't try to access negative indices
        print(movie[index])

# DISPLAY movies in watchlist that begin with "T"
def display_movies_beginning_with_t(movie):
    print('\nMovies in Watchlist that begin with "T":')
    sort_watchlist(movie) # sorting the watchlist in ascending order before displaying the movies that begin with "T"
    for index in movie:
        if index[0].upper() == 'T': # checking if the first letter of the movie title is "T" (case-insensitive)
            print(index)

# EXIT the program
def exit_program():
    exit = input('Are you sure you want to exit the program? (y/n): ')
    if exit == 'y':
        print('\nThank you for using the Movie Watchlist App. Goodbye!')
    elif exit == 'n':
        print('\nReturning to the main menu...')
    else:
        print('\nInvalid input. Please enter "y" or "n".')
        exit_program() # calling the exit_program function again to prompt the user for valid input
    return exit

# MAIN function to run the program
def main():
    display_header()
    exit = 'n'
    while exit == 'n':
        display_menu()
        choice = input('Enter your choice (1-15): ')
        if choice == '1':
            sort_watchlist(MOVIE_LIST_1) # passing the movie list as an argument to the sort_watchlist function to sort it before displaying it
            display_watchlist(MOVIE_LIST_1)
        elif choice == '2':
            print('\n**Watchlist 2**')
            create_add_movie_watchlist_2()
            sort_watchlist(MOVIE_LIST_2)
            display_watchlist(MOVIE_LIST_2)
        elif choice == '3':
            print('\n**Watchlist 2**')
            sort_watchlist(MOVIE_LIST_2)
            display_watchlist(MOVIE_LIST_2)
        elif choice == '4':
            MOVIE_LIST_3 = merge_watchlists(MOVIE_LIST_1, MOVIE_LIST_2) # calling the merge_watchlists function and passing the two watchlists as arguments to merge them into a new watchlist and assigning it to MOVIE_LIST_3
            sort_watchlist(MOVIE_LIST_3)
            display_watchlist(MOVIE_LIST_3)
        elif choice == '5':
            print('\n**Watchlist 3**')
            sort_watchlist(MOVIE_LIST_3)
            display_watchlist(MOVIE_LIST_3)

        # All the remaining selections pertain to the merged Watchlist 3 (the combined Watchlist 1 and Watchlist 2)

        elif choice == '6':
            print('\n**Watchlist 3**')
            number_of_movies(MOVIE_LIST_3)
        elif choice == '7':
            add_movie_end(MOVIE_LIST_3)
            display_watchlist(MOVIE_LIST_3) # display the updated watchlist after adding the movie to the end
        elif choice == '8':
            add_movie_beginning(MOVIE_LIST_3)
            display_watchlist(MOVIE_LIST_3) # display the updated watchlist after adding the movie to the beginning
        elif choice == '9':
            remove_movie(MOVIE_LIST_3)
        elif choice == '10':
            search_movie(MOVIE_LIST_3)
        elif choice == '11':
            display_movies_beginning_with_t(MOVIE_LIST_3)
        elif choice == '12':
            sort_watchlist_descending(MOVIE_LIST_3)
            display_watchlist(MOVIE_LIST_3) # display the updated watchlist after sorting it in descending order
        elif choice == '13':
            display_first_3_movies(MOVIE_LIST_3)
        elif choice == '14':
            display_last_3_movies(MOVIE_LIST_3)
        elif choice == '15':
             exit = exit_program()
        else:
            print('\nInvalid input. Please enter a number between 1 and 15.')


main() # calling the main function to start the program

# END OF PROGRAM