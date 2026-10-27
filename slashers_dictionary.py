#Famous horror slashers dictionary

movie_killers = {"halloween": "Michael Myers", "scream":"Ghostface", "texas massacre": "Leatherface", "friday the 13th": "Jason Voorhees", "hellraiser": "Pinhead", "chucky": "Chucky", "elm street": "Freddy Krueger"}

movie_cat = list(movie_killers) 
formated_cat = [i.title() for i in movie_cat]

print("Available horror movies are:", formated_cat)

flag = "yes"

while flag == "yes":
    fav_movie = " ".join(input("Enter your favorite horror movie to know the killer: ").split()).lower()
    error_msg = "Sorry, we couldn't find that movie in our database"
    error_msg2 = "Please enter yes or no"

    print(f"The killer of the movie {fav_movie.title()} is {movie_killers[fav_movie]}" if fav_movie in movie_killers else error_msg)

    while True:
        flag = input("Wanna try again?(yes/no) ").strip().lower()
        if flag not in ["yes", "no"]:
            print(error_msg2)
        else:
            break

print("Thanks for using our Killers Dictionary!!") 