import webbrowser


class Movie():
    """This class stores all movie related info."""

    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        """Initializes a movie instance."""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """Opens Webbrowser to play movie trailer."""
        webbrowser.open(self.trailer_youtube_url)
