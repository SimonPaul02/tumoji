from ytmusicapi import YTMusic
import json


class SongLyrics():
    music = YTMusic()


    def getSong(self, videoId: str, signatureTimestamp: int):
        return YTMusic.get_song(videoId, signatureTimestamp=0)

    def get_lyrics(self, browseId: str):
        dict = self.music.get_lyrics(browseId)
        return dict.get('lyrics').split()

    def get_lyrics_of_songs(self):
        dict = self.music.get_playlist(playlistId='RDCLAK5uy_lxAYpcccslny9wyba5G3CWsBBbNcna_Xs', limit=100)

        reduced_tracks = dict.get('tracks')[0]
        list_str = []
        for track, song in reduced_tracks.items():
            if track == 'title':
                # create helper list to put title and lyrics together into list_str
                list_helper = reduced_tracks["title"]
                # TODO How to get the browseId out of the songs?
                list_helper.append(self.get_lyrics("bla"))
                # putting together
                list_str.append(list_helper)
        return list_str
