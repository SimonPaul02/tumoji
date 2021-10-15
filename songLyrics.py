from ytmusicapi import YTMusic
import lyricsgenius as lg


class SongLyrics():
    music = YTMusic()
    list_helper = []

    genius = lg.Genius('Client_Access_Token_Goes_Here', skip_non_songs=True, excluded_terms=["(Remix)", "(Live)"],
                       remove_section_headers=True)

    def a(self):
        song = self.genius.search_song('Griechischer Wein', 'Udo Jürgens')
        print(song.lyrics)

        dict = self.music.get_playlist(playlistId="RDCLAK5uy_lxAYpcccslny9wyba5G3CWsBBbNcna_Xs", limit=100)

        reduced_tracks = dict.get('tracks')[0]
        list_str = []
        for track, song in reduced_tracks.items():
            if track == 'title':
                # create helper list to put title and lyrics together into list_str
                self.list_helper.append(reduced_tracks["title"])
                # TODO How to get the browseId out of the songs?
                self.list_helper.append(self.get_lyrics(browseId="OduynbTk_c"))
                # putting together
                list_str.append(self.list_helper)
        return list_str
