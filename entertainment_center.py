import fresh_tomatoes
import media

# here we are passing movie title, storyine, poster path and youtube url to
# the constructor of class Movie which is defined in media
# we are creating object for every single movie

Dangal = media.Movie("Dangal", "Dangal is a biopic film based on the life of a national wrestler",
                     "dangal.jpeg", "https://www.youtube.com/watch?v=x_7YlGv9u1g")

Sultan = media.Movie("Sultan", "About a wrestler who has problems in his professional and personal life",
                     "sultan.jpg", "https://www.youtube.com/watch?v=wPxqcq6Byq0")

JungleBook = media.Movie("Jungle Book", "Disney animation inspired by Rudyard Kiplings Mowgli story",
                         "junglebook.jpeg", "https://www.youtube.com/watch?v=HcgJRQWxKnw")

PK = media.Movie("PK", "It tells the story of an alien who comes to Earth on a research mission",
                 "pk.jpg", "https://www.youtube.com/watch?v=SOXWc32k4zA")

idiots = media.Movie("3 idiots", "The movie is loosely based on Chetan Bhagat's novel Five Point Someone",
                     "idiots.jpeg","https://www.youtube.com/watch?v=xvszmNXdM4w")

MSDhoni = media.Movie("M.S. Dhoni", "The untold story of Mahendra Singh Dhoni's journey from ticket collector to trophy collector",
                      "msdhoni.jpg", "https://www.youtube.com/watch?v=6L6XqWoS8tw")

# we are creating an array that stores all the objects
movies = [Dangal, Sultan, JungleBook, PK, idiots, MSDhoni]

# passing the array to the open_movies_page function defined in fresh_tomatoes
fresh_tomatoes.open_movies_page(movies)

