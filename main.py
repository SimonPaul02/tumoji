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
    synonyms = []

    for syn in wordnet.synsets("love"):
        for l in syn.lemmas():
            synonyms.append(l.name())

    print(set(synonyms))

    lyrics = '''I do the same thing I told you that I never would
I told you I'd change, even when I knew I never could
Know that I can't find nobody else as good as you
I need you to stay, need you to stay, hey (oh)
I get drunk, wake up, I'm wasted still
I realize the time that I wasted here
I feel like you can't feel the way I feel
Oh, I'll be fucked up if you can't be right here
Oh-oh-oh-whoa (oh-oh-whoa, oh-oh-whoa)
Oh-oh-oh-whoa (oh-oh-whoa, oh-oh-whoa)
Oh-oh-oh-whoa (oh-oh-whoa, oh-oh-whoa)
Oh, I'll be fucked up if you can't be right here
I do the same thing I told you that I never would
I told you I'd change, even when I knew I never could
Know that I can't find nobody else as good as you
I need you to stay, need you to stay, hey
I do the same thing I told you that I never would
I told you I'd change even when I knew I never could
Know that I can't find nobody else as good as you
I need you to stay, need you to stay, hey
When I'm away from you, I miss your touch (ooh-ooh)
You're the reason I believe in love
It's been difficult for me to trust (ooh-ooh)
And I'm afraid that I'ma fuck it up
Ain't no way that I can leave you stranded
'Cause you ain't ever left me empty-handed
And you know that I know that I can't live without you
So, baby, stay
Oh-oh-oh-whoa (oh-oh-whoa, oh-oh-whoa)
Oh-oh-oh-whoa (oh-oh-whoa, oh-oh-whoa)
Oh-oh-oh-whoa (oh-oh-whoa, oh-oh-whoa)
I'll be fucked up if you can't be right here
I do the same thing I told you that I never would
I told you I'd change, even when I knew I never could
Know that I can't find nobody else as good as you
I need you to stay, need you to stay, hey
I do the same thing I told you that I never would
I told you I'd change even when I knew I never could
Know that I can't find nobody else as good as you
I need you to stay, need you to stay, hey
Oh-oh-oh
I need you to stay, need you to stay, hey'''

    stopwords = nltk.corpus.stopwords.words("english")
    tokens = nltk.word_tokenize(lyrics)

    print("tokens: ")
    print(tokens)
    lyrics_without_sw = [w for w in tokens if not w.lower() in stopwords]
    lyrics_without_punct = [w for w in lyrics_without_sw if w.isalpha()]

    print("lyrics Without stop words: ")
    print(lyrics_without_punct)
    fdist = FreqDist(lyrics_without_punct)
    print("How many times each word")
    print(fdist.keys())
    print(fdist.values())
    print("most words")
    print(fdist.tabulate(20))


if __name__ == '__main__':
   # main()
   lyrics = songLyrics.SongLyrics()
   lyrics.get_lyrics_of_songs()
   print("done")
