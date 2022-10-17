# songs, artists and playlist

#  creating the song class
class Song:

    def __init__(self, title: str, artist: str, duration: int, category: str) -> None:
        self.title = title
        self.artist = artist
        self.duration = duration

        # song category can vary from HipHop, gospel, Rap, drill and so much more
        self.category = category


class Playlist:


    def __init__(self) -> None:
        self.playlist = []

    def display