import nltk
import songLyrics
from nltk import FreqDist
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.corpus import wordnet


# Sentiment Analysis
def is_positive(lyrics: str) -> bool:
    return SentimentIntensityAnalyzer.polarity_scores(lyrics)["compound"] > 0


# Main
def main():
    lyrics = songLyrics.SongLyrics()
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

    # print("tokens: ")
    # print(tokens)
    lyrics_without_sw = [w for w in tokens if not w.lower() in stopwords]
    lyrics_without_punct = [w for w in lyrics_without_sw if w.isalpha()]

    #   print("lyrics Without stop words: ")
    #  print(lyrics_without_punct)
    fdist = FreqDist(lyrics_without_punct)
    # print("How many times each word")
    #  print(fdist.keys())
    # print(fdist.values())
    print("most words")
    print(fdist.tabulate(20))


if __name__ == '__main__':
    main()
    print("done")
