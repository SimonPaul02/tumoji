from ytmusicapi import YTMusic
import lyricsgenius as lg


class SongLyrics:

    def __init__(self, playlist):
        self.playlist = playlist

    music = YTMusic()
    final_list = []

    genius = lg.Genius('Client_Access_Token_Goes_Here', skip_non_songs=True, excluded_terms=["(Remix)", "(Live)"],
                       remove_section_headers=True)

    def get_lyrics_from_genius(self, title, author):
        try:
            song = self.genius.search_song(artist=author, title=title)
        except:
            return []

        if song == None:
            return []
        return song.lyrics.lower()

    def get_lyrics_of_songs(self):
        playlist = ""
        while True:
            try:
                playlist = self.music.get_playlist(playlistId=self.playlist, limit=4)
                break
            except:
                print("connection error, trying again")

        tracks = playlist.get('tracks')
        for track in tracks:
            title = ""
            author = ""
            song_details = []
            # create helper list to put title and lyrics together into final_list
            title = track["title"]
            author = track["artists"][0]
            author = list(author.items())[0][1]
            index = title.find('(')
            if index == -1:
                index = title.find("[")

            lyrics = []
            if index > 0:
                lyrics = self.get_lyrics_from_genius(title[0:index], author)
            else:
                lyrics = self.get_lyrics_from_genius(title, author)
            if not lyrics == [] and lyrics is not None:
                song_details.append(author)
                song_details.append(title)
                song_details.append(lyrics)
                # putting together
                self.final_list.append(song_details)

            if len(self.final_list) == 10:
                return self.final_list
        return self.final_list
