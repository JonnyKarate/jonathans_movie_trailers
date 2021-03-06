import media
import fresh_tomatoes

# Seven Samurai movie: movie title, storyline, poster image and trailer
seven_samurai = media.Movie(
    "Seven Samurai",
    "Seven samurai defend a village against bandits.",
    "http://www.gstatic.com/tv/thumb/dvdboxart/5588/p5588_d_v7_aa.jpg",
    "https://youtu.be/VDUjDPt9w0w"
    )

# The Princess Bride movie: movie title, storyline, poster image and trailer
the_princess_bride = media.Movie(
    "The Princess Bride",
    "Based on William Goldman's novel of the same name, "
    "The Princess Bride is staged as a book read by grandfather (Peter Falk)"
    "to his ill grandson (Fred Savage). Falk's character assures "
    "a romance-weary Savage that the book has much more to deliver "
    "than a simpering love story, including but not limited to "
    "fencing, fighting, torture, death, true love, giants, and pirates.",
    "https://images-na.ssl-images-amazon.com/images/I/81nq1uq4wyL._SY445_.jpg",
    "https://www.youtube.com/watch?v=WNNUcHRiPS8"
    )

# Ratatouille movie: movie title, storyline, poster image and trailer
ratatouille = media.Movie(
    "Ratatouille",
    "A rat is a chef in Paris",
    "https://www.youtube.com/watch?v=c3sBBRxDAqk",
    "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg"
    )

# The Wackness movie: movie title, storyline, poster image and trailer
the_wackness = media.Movie(
    "The Wackness",
    "A teenage weed dealer in New York trades dime bags for therapy sessions.",
    "https://goo.gl/N7MpD7",
    "https://www.youtube.com/watch?v=fEjw-OkMv3w",
    )

# The Naked Gun movie: movie title, storyline, poster image and trailer
the_naked_gun = media.Movie(
    "The Naked Gun",
    "A rather clueless police detective, tries to foil a plot "
    "to turn innocent people into assassins through mind control.",
    "http://www.gstatic.com/tv/thumb/movieposters/11300/p11300_p_v7_aa.jpg",
    "www.youtube.com/watch?v=eJEmtLxkEoI"
    )

# Vertigo movie: movie title, storyline, poster image and trailer
vertigo = media.Movie(
    "Vertigo",
    "A detective with a fear of heights is forced to retire.",
    "https://upload.wikimedia.org/wikipedia/commons/7/75/Vertigomovie_restoration.jpg",
    "www.youtube.com/watch?v=Z5jvQwwHQNY"
    )

# Set the movies that will be passed to the media file
movies = [
    seven_samurai,
    the_princess_bride,
    ratatouille,
    the_wackness,
    the_naked_gun,
    vertigo
    ]

# Open the HTML file in a webbrowser via fresh_tomatoes.py
fresh_tomatoes.open_movies_page(movies)
