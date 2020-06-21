# Incomplete app!

# Python course Milstone-1 asignment
import cv2

def add_movie():
    print("YOU WANT TO ADD A NEW MOVIE")
    moviename = input("Specify name of the movie: ").capitalize()
    movieyear = input("Specify production year for movie: ")
    moviedirector = input("Specify who directed the movie: ").capitalize()
    movielib = input("Specify the moviefile: ")

    movie_list.append({"m_name": moviename, "m_director": moviedirector, "m_prod_year": movieyear, "movie": movielib})
    print("Movie has been added to libraray")
    print(moviename)
    type(moviename)
    for movie in movie_list:
        print(movie)

def find_movie():
    q = True
    while q == True:
        seach_name = input("Specify title on movie, (Enter for none):  ").lower()
        seach_year = input("Specify the year on movie, (Enter for none) :  ").lower()
        seach_director = input("Specify who has directed the movie, (Enter for none)S:  ").lower()
        if seach_name == "" and seach_year == "" and seach_director == "":
            print(" Specify at lease one search criteria")
            print("\n")
        else:
            q = False

    for movie in movie_list:
        if (seach_name.lower() == movie["m_name"].lower() or (seach_name == '')) and (
                seach_director.lower() == movie["m_director"].lower() or (seach_director == '')) and (
                seach_year.lower() == movie["m_prod_year"].lower() or (seach_year == '')):
            print("Movies found:")
            print(f"Movie: {movie['m_name']} # Production year: {movie['m_prod_year']} Directed by: {movie['m_director']}")


def list_all_movies():
    for moviee in movie_list:
        print("MOVIE TITEL: ", moviee["m_name"])


def view_movie():
    movie_to_watch = input("Please select the movie to match:  ").lower()
    print("You want to watch movie: ")

    for movie in movie_list:
        if (movie_to_watch.lower() == movie["m_name"].lower() ):
            print("Movies found:")
            print(f"Movie: {movie['m_name']} # Production year: {movie['m_prod_year']} Directed by: {movie['m_director']}")
            print(f"This is the movie file: {movie['movie']}")
            watchh = movie['movie']

    cap = cv2.VideoCapture(watchh)

    ret = True
    while ret:
        if cap.isOpened():
            ret, frame = cap.read()
        if ret:
            cv2.imshow("Movie window player",frame)
            if cv2.waitKey(1) == 27:
                break
        else:
            break

    cap.release()
    cv2.destroyAllWindows()

movie_list = [
    {"m_name": "De Urørlige", "m_director": "kaj", "m_prod_year" :"2011" ,"movie" :"file_example_AVI_1280_1_5MG.avi"},
    {"m_name": "Bowling for Columbine", "m_director":"Kali","m_prod_year":"2025", "movie":"file_example_AVI_1280_1_5MG.avi"},
    {"m_name": "Der Untergang", "m_director": "Kali","m_prod_year": "2025", "movie":"file_example_AVI_1280_1_5MG.avi" },
    {"m_name": "Kongekabale", "m_director":"Kali", "m_prod_year": "2025" , "movie":"file_example_AVI_1280_1_5MG.avi"},
    {"m_name": "E.T.", "m_director":"Steven Spielberg", "m_prod_year":"1982", "movie":"sample-avi-file.avi"},
    {"m_name": "The Godfather", "m_director":"Mario Puzo ", "m_prod_year":"1972", "movie":"file_example_AVI_1280_1_5MG.avi"},
    {"m_name": "Casabalca", "m_director": "Michael Curtiz", "m_prod_year":"1942", "movie":"file_example_AVI_1280_1_5MG.avi"},
    {"m_name": "Psycho", "m_director": "Alfred Hitchkock", "m_prod_year":"1960", "movie":"file_example_AVI_1280_1_5MG.avi"},
    {"m_name": "AAA", "m_director": "2", "m_prod_year": "1960", "movie": "file_example_AVI_1280_1_5MG.avi"},
    {"m_name": "AAA", "m_director": "2", "m_prod_year": "1960", "movie": "file_example_AVI_1280_1_5MG.avi"}
]

print("**************   Welcome to you movie libary   *****************'")
print("Menu")
running = True

while running:
#view_movie()

    operation = input("Please enter  'find', 'add', 'list',  'view' or 'q' to end the program' ").lower()
    print("You have chosen: ",operation)

    if operation == "view":
        view_movie()

    if operation == 'find':

        find_movie()

    if operation == "add":
        print("add")
        add_movie()

    if operation == "list":
        print("Movies in Movie-Library: ")
        list_all_movies()

    if operation == "q":
        print("Look forward to see you next time, bye bye")
        break

    if operation != "view" and operation != "find" and operation != "add" and operation != "list" and operation != "end":
        print("Please make a correct selection")

    print("\n")

    #Specifications:
    # create at movie library , with parameters: Movie title,  director, production year, the movie
    # DONE Must allow to add new movies
    # DONE Must allow the user to view all movies in collection
    # DONE Must allow the user to search for a movie using any og the listed parameters


