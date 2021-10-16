import codecs

import nltk
from urllib3.filepost import writer

import songLyrics
#import gui
from nltk import FreqDist
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.corpus import wordnet
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer

import numpy as np
import csv
import pandas as pd

# Sentiment Analysis
def is_positive(lyrics: str) -> bool:
    return SentimentIntensityAnalyzer.polarity_scores(lyrics)["compound"] > 0


# Main
def main():
    study_playlist = "RDCLAK5uy_nZJzoZEBYRptA2XXskbxGTvKkevapT_F4"  # 📕
    party_playlist = "RDCLAK5uy_n4PuqfjXs63tz7E3lEs2av_rSBmuJqf-k"  # 🍾
    relax_playlist = "RDCLAK5uy_mdwsZFtQhJyGQPuQA612VoRPXp-OJfzx8"  # 😎
    romance_playlist = "RDCLAK5uy_l1oO11DBO4FD8U7bOrqUKK5Y_PkISUMQM"  # ❤️
    good_mood_playlist = "RDCLAK5uy_kvmdYWgmu7MBsrWUzv53AyF02ytmE18bo"  # 😂
    sad_mood_playlist = "PLLIVqphyPGcWicpB3eXYDpXFY5KuuQs6_"  # ☹️

    lyrics = songLyrics.SongLyrics(good_mood_playlist)
    song_data_set = lyrics.get_lyrics_of_songs()

    fields = ["Author", "Title", "Lyrics"]
    # with codecs.open('goodMusicPlaylist.csv', 'w', encoding='UTF-8') as f:
    ''' for row in song_data_set:
         for x in row:
             f.write(str(x) + ';')
         f.write('\n')

               
         synonyms = []
         for syn in wordnet.synsets("love"):
             for l in syn.lemmas():
                 synonyms.append(l.name())
         print(set(synonyms))
        '''

    vocal_tics = ['ooh']
    porter = PorterStemmer()
    print(len(song_data_set))
    for x in range(0,len(song_data_set)):
        song_author = song_data_set[x][0]
        song_name = song_data_set[x][1]
        song_lyrics = song_data_set[x][2]

        df = pd.DataFrame(song_data_set, columns = ['song_author','song_name','song_lyrics'])
        df['song_lyrics'] = df['song_lyrics'].str.replace('\n',' nl ')
        print(df)
        # saving the DataFrame as a CSV file
        gfg_csv_data = df.to_csv('GfG.csv', index = True)
        print('\nCSV String:\n', gfg_csv_data)

        song_lyrics_array = []
        #print(song_lyrics.split())
        stopwords = nltk.corpus.stopwords.words("english")
        tokens = nltk.word_tokenize(song_lyrics)

        lyrics_without_sw = [w for w in tokens if not w.lower() in stopwords]
        lyrics_without_punct = [w for w in lyrics_without_sw if w.isalpha()]
        lyrics_without_vt = [w for w in lyrics_without_punct if not w in vocal_tics]

        lyrics_stemmed = [porter.stem(word) for word in lyrics_without_vt]
        fdist = FreqDist(lyrics_stemmed)

        # print("song_name: " + song_name)
        # print("song_author: " + song_author)
        # print("song_lyrics: " + song_lyrics)
        # print(tokens)
        # print("song_tokens: " + ''.join(tokens))
        print("most words")
        print(fdist.tabulate(5))


if __name__ == '__main__':
    main()
    print("done")
