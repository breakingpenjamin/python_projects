#
# Exam 3
# Name: Keyshawn Curtis
# Musicians and their Songs Program
# 05/11/2026

'''
This program merges two dictionaries of musicians and popular songs they made into one dictionary. Then the dictionary 
is modified by various methods.
'''

# Musician Dictionaries
Musicians_1 = {'Michael Jackson':'Man in the Mirror',
              'AC/DC':'Thunderstruck',
              'Limp Bizkit':'Break Stuff',
              'Breaking Benjamin':'The Diary of Jane',
              'Eminem':'Lose Yourself',
              'Yuuri':'Curtain Call'}

Musicians_2 = {}

Musicians_3 = {}

# start up banner
def startup_banner():
    print()
    print('                =======================================')
    print('                =======================================')
    print('                ==            Welcome to             ==')
    print('                == Musicians and their Popular Songs ==')
    print('                ==        Organization Program       ==')
    print('                =======================================')
    print('                =======================================')
    print()

# choice menu
def choice_menu():
    print()
    print('                 *************************************')
    print('                 * Musicians and their Popular Songs *')
    print('                 *************************************')
    print('Menu Choices:')
    print(' 1. Display all Musicians and their Popular Songs, stored in dictionary Musicians_1')
    print(' 2. Create and/or Add Musicians and their Popular Songs to dictionary Musicians_2')
    print(' 3. Display all the Musicians and Song pairs stored in dictionary Musicians_2')
    print(' 4. Merge Musicians_1 and Musicians_2 dictionaries, into Musicians_3')
    print('==============================================================================')
    print('  All the remaining selections pertain to the merged dictionary (Musicians_3) ')
    print('==============================================================================')
    print(' 5. Display all Musicians and their Popular Songs, stored in dictionary.')
    print(' 6. Display how many Musicians and their Popular Songs are stored in dictionary.')
    print(' 7. Display only the Musicians, stored in dictionary.')
    print(' 8. Display only the Popular Songs, stored in dictionary.')
    print(' 9. Display all the Musicians and their Popular Songs, in dictionary (sorted by Songs)')
    print('10. Add a new Musician and their Popular Song to dictionary.')
    print("11. Change a Musician's Popular Song in dictionary.")
    print('12. Remove a Musician and their Popular Song from dictionary.')
    print('13. Look up a Musician in dictionary.')
    print('14. Look up a Popular Song in dictionary.')
    print('15. Search for song in dictionary and display associated musician.')
    print('16. Check for Musician associated with Popular Song. If found, display the song (opt to override). If not, opt to add new pair.')
    print('17. Display all Musicians (in descending order))')
    print('18. Display all Popular Songs (in descending order))')
    print('19. Clear all Musicians and their Popular Songs from dictionary.')
    print('20. Exit the Program')


    choice = int(input('Please enter your choice: '))
    while choice < 1 or choice > 20:
        choice = int(input('Enter a valid choice. Select a choice between 1-20: '))

    return choice

# display all musicians and their songs (Musicians_1)
def display_all(Musicians_1):
    print()
    # print('Musician\tSong')
    print(f'\n{"Musician":<20}{"Song":<20}')
    print('----------------------------------------')

    for key,value in Musicians_1.items():
        print(f'{key:<20}{value:<20}')
    print()

# merge two dictionaries into one dictionary
def merge_dictionaries(Musicians_1, Musicians_2):
    Musicians_3 = {**Musicians_1, **Musicians_2} # Merge the two dictionaries into one dictionary
    return Musicians_3

# sort dictionary by key in ascending order
def sort_asc_key(musician_song):
    sorted_dict = dict(sorted(musician_song.items()))
    return sorted_dict

# sort dictionary by value in ascending order
def sort_asc_value(musician_song):
    sorted_dict = dict(sorted(musician_song.items(), key=lambda item: item[1])) # Sort the dictionary by value (song name) in ascending order
    return sorted_dict

# add musician and song/create new dictionary
def add_musician_and_song(musician_song):
    print()
    print()
    musician = input('Enter the name of the Musician: ')
    musician = musician.title() # Convert the input to title case
    print()
    song = input('Enter the name of the Popular Song: ')
    song = song.title() # Convert the input to title case
    print()

    if musician not in musician_song:
        musician_song[musician] = song # Add the musician and song to the dictionary
        musician_song = sort_asc_key(musician_song) # Sort the dictionary by musician name in ascending order
        display_all(musician_song) # Display the updated dictionary
    else:
        print(f'{musician} is already in the dictionary with the song "{musician_song[musician]}".')
        print('No changes have been made to the dictionary.')

# change a musician's song
def change_song(musician_song):
    print()
    print()
    musician = input('Enter the name of the Musician whose song you want to change: ')
    if musician == 'AC/DC':
        musician = 'AC/DC' # Handle the special case for AC/DC to ensure it is entered correctly
    else:
        musician = musician.title() # Convert the input to title case
    print()
    print()

    if musician in musician_song:
        new_song = input(f'Enter the new song for {musician}: ')
        new_song = new_song.title() # Convert the input to title case
        print()
        musician_song[musician] = new_song # Update the song for the specified musician in the dictionary
        musician_song = sort_asc_key(musician_song) # Sort the dictionary by musician name in ascending order
        display_all(musician_song) # Display the updated dictionary
    else:
        print(f'{musician} is not found in the dictionary.')
        print('No changes have been made to the dictionary.')

# remove a musician and their song
def remove_musician_song(musician_song):
    print()
    print()
    musician = input('Enter the name of the Musician you want to remove: ')
    if musician == 'AC/DC':
        musician = 'AC/DC' # Handle the special case for AC/DC to ensure it is entered correctly
    else:
        musician = musician.title() # Convert the input to title case
    print()
    print()
    decide = input(f'Are you sure you want to remove {musician}? (Enter Y to continue): ')
    decide = decide.title() # Convert the input to title case
    if decide == 'Y':
        if musician in musician_song:
            del musician_song[musician] # Remove the specified musician and their song from the dictionary
            print(f'{musician} has been removed from the dictionary.')
            print()
            display_all(musician_song) # Display the updated dictionary
        else:
            print()
            print()
            print('---DELETION CANCELED---')
            print(f'{musician} is not found in the dictionary.')
            print()

# confirm if a musician is in the dictionary and display their song, if not opt to add the musician and song to the dictionary
def confirm_musician(musician_song):
    print()
    print()
    musician = input('Enter the name of the Musician you want to look up: ')
    if musician == 'AC/DC':
        musician = 'AC/DC' # Handle the special case for AC/DC to ensure it is entered correctly
    else:
        musician = musician.title() # Convert the input to title case
    print()
    print()

    if musician in musician_song:
        print()
        print(f'{musician} is in the dictionary with the song.')
        print()
    else:
        print(f'{musician} is not found in the dictionary.')
        print()

# confirm if a song is in the dictionary and display the musician, if not opt to add the musician and song to the dictionary
def confirm_song(musician_song):
    print()
    print()
    song = input('Enter the song name to check if in the dictionary: ')
    song = song.title()
    print()
    
    if song in musician_song.values(): # to check if the value is in the dictionary use .values() method
        print()
        print(f'The Song {song} is in the dictionary')
        print()
    else:
        print(f'The Song {song} is not found in the dictionary')
        print()

# number of musicians and songs in the dictionary
def num_artist(musician_song):
    print()
    print()
    print()
    print('-------------------------------------------------------------------')
    print(f'     There are {len(musician_song)} Musicians/Song pairs in the dictionary',)
    print('-------------------------------------------------------------------')
    print()

# display only the musicians in the dictionary
def musician_names(musician_song):
    print()
    print()
    print('Musicians:')
    print('------------------')
    names = musician_song.keys()
    for key in names: # Iterate through the keys of the dictionary and print each key (musician name)
        print(key)
    print('---------------------------------------')
    print()

# display only the songs in the dictionary
def song_names(musician_song):
    print()
    print()
    print('Songs:')
    print('------------------')
    songs = musician_song.values()
    for value in songs: # Iterate through the values of the dictionary and print each value (song name)
        print(value)
    print('---------------------------------------')
    print()

# search for song in dictionary and display associated musician
def search_song(musician_song):
    print()
    print()
    song = input('Enter the name of the Song you want to look up: ')
    song = song.title() # Convert the input to title case
    print()

    if song in musician_song.values(): # to check if the value is in the dictionary use .values() method
        for key, value in musician_song.items():
            if value == song:
                print(f'The author of "{song}" is {key}.')
                print()
    else:
        print(f'The song "{song}" is not found in the dictionary.')
        print()

# display musicians in descending order
def sort_desc_musician(musician_song):
    print()
    print()
    print('Musicians (Descending Order):')
    print('-----------------------------------------------------')
    sorted_dict = dict(sorted(musician_song.items(), reverse=True)) # Sort the dictionary by key (musician name) in descending order
    return sorted_dict

# display songs in descending order
def sort_desc_song(musician_song):
    print()
    print()
    print('Songs (Descending Order):')
    print('-----------------------------------------------------')
    sorted_dict = dict(sorted(musician_song.items(), key=lambda item: item[1], reverse=True)) # Sort the dictionary by value (song name) in descending order
    return sorted_dict

# determine if popular song is associated with a musician. If found, display the song, if not opt to override song.
def check_song(musician_song):
    print()
    print()
    musician = input('Enter the name of the Musician you want to check: ')
    if musician == 'AC/DC':
        musician = 'AC/DC' # Handle the special case for AC/DC to ensure it is entered correctly
    else:
        musician = musician.title() # Convert the input to title case
    print()

    if musician in musician_song:
        print(f'{musician} is in the dictionary & associated with the song "{musician_song[musician]}".')
        decide = input(f"Would you like to change {musician}'s song? (Enter Y to continue): ")
        decide = decide.title() # Convert the input to title case
        if decide == 'Y':
            print('-----------------------------------------------------------')
            change_song(musician_song) # Call the function to change the song for the specified musician in the dictionary
        print()
    else:
        print(f'{musician} is not found in the dictionary.')
        print()
        decide = input(f"Would you like to add {musician}'s and their Popular Song to the dictionary? (Enter Y to continue): ")
        decide = decide.title() # Convert the input to title case
        if decide == 'Y':
            add_musician_and_song(musician_song) # Call the function to add a new musician and song to the dictionary
        else:
            print()
            print('Continuing Program')
            print()

# clear all musicians and songs from the dictionary
def clear_dictionary(musician_song):
    print()
    print()
    decide = input('Are you sure you want to clear all Musicians and their Popular Songs from the dictionary? (Enter Y to continue): ')
    decide = decide.title() # Convert the input to title case
    if decide == 'Y':
        musician_song.clear() # Clear all items from the dictionary
        print('All Musicians and their Popular Songs have been cleared from the dictionary.')
        print()
        display_all(musician_song) # Display the updated dictionary (which will be empty)
    else:
        print()
        print()
        print('---CLEARING CANCELED---')
        print()

# exit the program
def exit_program():
    print()
    print()
    decide = input('Are you sure you would like to quit the program?\nEnter Y to quit else type any key: ')
    decide = decide.title()
    if decide == 'Y':
        print()
        print()
        print('exiting....')
        print('Thank you for using Musicians and Songs organizing program!')
        print('Have an heheee-- Amazing Day!')
        return 20
    else:
        print()
        print('Continuing Program')
        return 0

# main function
def main():
    startup_banner()
    choice = 0

    while choice != 20:
        choice = choice_menu()

        if choice == 1:
            display_all(Musicians_1)
        elif choice == 2:
            add_musician_and_song(Musicians_2)
            Another = input('Would you like to add another Musician and their Popular Song to the dictionary? (Y/N): ')
            Another = Another.title()
            while Another == 'Y':
                add_musician_and_song(Musicians_2)
                Another = input('Would you like to add another Musician and their Popular Song to the dictionary? (Y/N): ')
                Another = Another.title()
        elif choice == 3:
            display_all(Musicians_2)
        elif choice == 4:
            Musicians_3 = merge_dictionaries(Musicians_1, Musicians_2)
            Musicians_3 = sort_asc_key(Musicians_3) # Sort the merged dictionary by musician name in ascending order
            print('\nThe two dictionaries have been merged into one dictionary.')
            display_all(Musicians_3)
            print()
        elif choice == 5:
            Musicians_3 = sort_asc_key(Musicians_3) # Sort the dictionary by musician name in ascending order
            display_all(Musicians_3)
        elif choice == 6:
            num_artist(Musicians_3)
        elif choice == 7:
            Musicians_3 = sort_asc_key(Musicians_3) # Sort the dictionary by musician name in ascending order
            musician_names(Musicians_3)
        elif choice == 8:
            Musicians_3 = sort_asc_value(Musicians_3) # Sort the dictionary by musician name in ascending order
            song_names(Musicians_3)
        elif choice == 9:
            Musicians_3 = sort_asc_value(Musicians_3) # Sort the dictionary by song name in ascending order
            display_all(Musicians_3)
        elif choice == 10:
            add_musician_and_song(Musicians_3)
        elif choice == 11:
            change_song(Musicians_3)
        elif choice == 12:
            remove_musician_song(Musicians_3)
        elif choice == 13:
            confirm_musician(Musicians_3)
        elif choice == 14:
            Musicians_3 = sort_asc_value(Musicians_3) # Sort the dictionary by song name in ascending order
            confirm_song(Musicians_3)
        elif choice == 15:
            search_song(Musicians_3)
        elif choice == 16:
            check_song(Musicians_3)
        elif choice == 17:
            Musicians_3 = sort_desc_musician(Musicians_3)
            musician_names(Musicians_3)
        elif choice == 18:
            Musicians_3 = sort_desc_song(Musicians_3)
            song_names(Musicians_3)
        elif choice == 19:
            clear_dictionary(Musicians_3)
        elif choice == 20:
            exit_program()

if __name__ == "__main__":
    main()