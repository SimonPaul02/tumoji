import nltk
import songLyrics
import gui
from nltk import FreqDist
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.corpus import wordnet


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

    """
    synonyms = []
    for syn in wordnet.synsets("love"):
        for l in syn.lemmas():
            synonyms.append(l.name())
    print(set(synonyms))
   """

    lyrics = song_data_set[0][2]

    stopwords = nltk.corpus.stopwords.words("english")
    tokens = nltk.word_tokenize(lyrics)

    lyrics_without_sw = [w for w in tokens if not w.lower() in stopwords]
    lyrics_without_punct = [w for w in lyrics_without_sw if w.isalpha()]

    fdist = FreqDist(lyrics_without_punct)

    print("most words")
    print(fdist.tabulate(20))


if __name__ == '__main__':
    main()
    print("done")
