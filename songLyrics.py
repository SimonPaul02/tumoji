from ytmusicapi import YTMusic
import lyricsgenius as lg


class SongLyrics():
    music = YTMusic()
    final_list = []
    song = ""

    genius = lg.Genius('Client_Access_Token_Goes_Here', skip_non_songs=True, excluded_terms=["(Remix)", "(Live)"],
                       remove_section_headers=True)

    def get_lyrics_from_genius(self, title, author):
        song = self.genius.search_song(artist=author, title=title)
        print(type(song))
        return song.lyrics.split()

    def get_lyrics_of_songs(self):

        playlist = self.music.get_playlist(playlistId="RDCLAK5uy_lxAYpcccslny9wyba5G3CWsBBbNcna_Xs", limit=100)
        reduced_tracks = playlist.get('tracks')[0]
        title = ""
        author = ""
        for track, lyrics in reduced_tracks.items():
            list_helper = []
            if track == 'title':
                # create helper list to put title and lyrics together into final_list
                title = reduced_tracks["title"]
            if track == 'artists':
                author = reduced_tracks["artists"][0]
                author = list(author.items())[0][1]
                index = title.find('(')
                if (index > 0):
                    lyrics = self.get_lyrics_from_genius(title[0:index], author)
                else:
                    lyrics = self.get_lyrics_from_genius(title, author)
                list_helper.append(author)
                list_helper.append(title)
                list_helper.append(lyrics)
                # putting together
                self.final_list.append(list_helper)

        return self.final_list
