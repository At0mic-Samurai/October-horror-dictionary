#Famous horror slashers dictionary

movie_killers = {"halloween": "Michael Myers", "scream":"Ghostface", "texas massacre": "Leatherface", "friday the 13th": "Jason Voorhees", "hellraiser": "Pinhead", "chucky": "Chucky", "elm street": "Freddy Krueger"}

movie_cat = list(movie_killers) # This takes the dictionary keys by default and converts it to a list
formated_cat = [i.title() for i in movie_cat] # List comprehension to save space. Takes every item from previous list and capitalize the first letter of each word

print("Available horror movies are:", formated_cat)

flag = "yes"

while flag == "yes": # Primary loop 
    fav_movie = " ".join(input("Enter your favorite horror movie to know the killer: ").split()).lower() # Probably the most important part of the script. It makes the user entry case and space insensitive
    error_msg = "Sorry, we couldn't find that movie in our database"
    error_msg2 = "Please enter yes or no"

    print(f"The killer of the movie {fav_movie.title()} is {movie_killers[fav_movie]}" if fav_movie in movie_killers else error_msg) # Use of ternary operators and accessing dictionary values to format the output

    while True: # Inner validation loop
        flag = input("Wanna try again?(yes/no) ").strip().lower()
        if flag not in ["yes", "no"]:
            print(error_msg2)
        else:
            break

print("Thanks for using our Killers Dictionary!!") 
