from ytmusicapi import YTMusic
import json


def getPlaylist():
    return YTMusic.get_playlist("RDCLAK5uy_k5faEHND0iXJljeASESqJ3A8UtRr2FL00", 100)

def getSong(videoId:str, signatureTimestamp:int):
    return YTMusic.get_song(videoId, signatureTimestamp=0)


#TODO get browseId
def getLyrics(browseId:str):
    dict = YTMusic.get_lyrics(browseId)
    return dict["lyrics"].split()