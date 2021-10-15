import nltk
import songLyrics
from nltk import FreqDist
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import RegexpTokenizer


# Sentiment Analysis
def is_positive(lyrics: str) -> bool:
    return SentimentIntensityAnalyzer.polarity_scores(lyrics)["compound"] > 0


# Main
def main():
    lyrics = '''O! say can you see
by the dawn’s early light,
What so proudly we hailed
at the twilight’s last gleaming,
Whose broad stripes and bright stars
through the perilous fight,
O’er the ramparts we watched,
were so gallantly streaming?
And the rockets’ red glare,
the bombs bursting in air,
Gave proof through the night
that our flag was still there;
O! say does that star-spangled
banner yet wave,
O’er the land of the free
and the home of the brave?'''

    stopwords = nltk.corpus.stopwords.words("english")
    tokens = nltk.word_tokenize(lyrics)

    print("tokens: ")
    print(tokens)
    lyricsWithoutSW = [w for w in tokens if not w.lower() in stopwords]
    lyricsWithoutSW = [w for w in lyricsWithoutSW if w.isalpha()]

    print("lyrics Without stop words: ")
    print(lyricsWithoutSW)
    fdist = FreqDist(lyricsWithoutSW)
    print("How many times each word")
    print(fdist.keys())
    print(fdist.values())
    print("most words")
    print(fdist.tabulate(10))


if __name__ == '__main__':
    main()
    songList = songLyrics.get_lyrics_of_songs()
    print("done")
