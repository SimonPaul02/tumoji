from ytmusicapi import YTMusic
import json


def get_lyrics_of_songs():
    dict = YTMusic.get_playlist('RDCLAK5uy_k5faEHND0iXJljeASESqJ3A8UtRr2FL00', 100)
    reduced_tracks = dict.get('tracks')[0]
    list_str = []
    for track,song in reduced_tracks.items():
        if track == 'title':
            #create helper list to put title and lyrics together into list_str
            list_helper = reduced_tracks["title"]
            #TODO How to get the browseId out of the songs?
            list_helper.append(get_lyrics())
            #putting together 
            list_str.append(list_helper)
    return list_str
    

def getSong(videoId:str, signatureTimestamp:int):
    return YTMusic.get_song(videoId, signatureTimestamp=0)

def get_lyrics(browseId:str):
    dict = YTMusic.get_lyrics(browseId)
    return dict.get('lyrics').split()

def main():
    print(get_lyrics_of_songs)

if __name__ == '__main__':
    main()