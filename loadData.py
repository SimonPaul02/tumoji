import numpy as np
import pandas as pd
import songLyrics

class loadData:
    data = np.array

    playlist_ID = {'study':'RDCLAK5uy_nZJzoZEBYRptA2XXskbxGTvKkevapT_F4',
                   'party':'RDCLAK5uy_n4PuqfjXs63tz7E3lEs2av_rSBmuJqf-k',
                   'relax':'RDCLAK5uy_mdwsZFtQhJyGQPuQA612VoRPXp-OJfzx8',
                   'good_mood':'RDCLAK5uy_kvmdYWgmu7MBsrWUzv53AyF02ytmE18bo',
                   'sad_mood':'PLLIVqphyPGcWicpB3eXYDpXFY5KuuQs6_'}

    # study_playlist = "RDCLAK5uy_nZJzoZEBYRptA2XXskbxGTvKkevapT_F4"  # 📕
    # party_playlist = "RDCLAK5uy_n4PuqfjXs63tz7E3lEs2av_rSBmuJqf-k"  # 🍾
    # relax_playlist = "RDCLAK5uy_mdwsZFtQhJyGQPuQA612VoRPXp-OJfzx8"  # 😎
    # romance_playlist = "RDCLAK5uy_l1oO11DBO4FD8U7bOrqUKK5Y_PkISUMQM"  # ❤️
    # good_mood_playlist = "RDCLAK5uy_kvmdYWgmu7MBsrWUzv53AyF02ytmE18bo"  # 😂
    # sad_mood_playlist = "PLLIVqphyPGcWicpB3eXYDpXFY5KuuQs6_"  # ☹️

    lyrics = songLyrics.SongLyrics(playlist_ID['good_mood'])
    song_data_set = lyrics.get_lyrics_of_songs()

    #take input from api and add to array
    def create_arrray():
        return 

