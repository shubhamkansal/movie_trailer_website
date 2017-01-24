import webbrowser

class Movie():
    """ -> This class provides a way to store movie related information
        -> __init__ is constructor
        -> self is the object name that is the calling the constructor
        -> title, storyline, poster_image_url and trailer_youtube_url are instance variables """
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
