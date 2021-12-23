import matplotlib
import matplotlib.pyplot as plt
import nltk
from numpy import mat
from wordcloud import WordCloud

matplotlib.use("Agg")

from string import punctuation
from nltk.corpus import stopwords

nltk.download("stopwords")


def dataDictionary(data):
    dic = {str(i): [] for i in range(1, 13)}
    for i in data:
        dic[str(i[0])].append(i[1])
    return dic


def retrieveMonths(dic, args) -> list:
    words = list()
    for month in args:
        for question in dic[str(month)]:
            for word in question.split():
                words.append(word)
    return words


def nltkfilter(words):
    engStopWords = stopwords.words("english")
    fwords = [
        word
        for word in words
        if word not in punctuation and word not in engStopWords and len(word) >= 4
    ]
    return fwords


def get_words(file_path) -> list:
    f = open(file_path, errors="ignore")
    content = f.read()
    content_list = content.split()
    for i in range(len(content_list)):
        content_list[i] = content_list[i].lower()
    return content_list


def createWordCloud(words, numWords, filepath):
    filtered_words = nltkfilter(words)
    wc = WordCloud(
        max_font_size=45, max_words=numWords, background_color="white", scale=2.0
    )
    wordcloud = wc.generate_from_text(" ".join(filtered_words))
    wordcloud.to_file(filepath)


def plotFrequency(words, numWords, myTitle, filepath):
    plt.ioff()
    fig = plt.figure()

    plt.gcf().subplots_adjust(bottom=0.15)
    filtered_words = nltkfilter(words)
    freq_dist = nltk.FreqDist(filtered_words)

    freq_dist.plot(numWords, cumulative=False)
    plt.title(myTitle)
    fig.savefig(filepath, bbox_inches="tight")


def customPlotFreq(data, months, filepath):
    dicMonths = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December",
    }
    s = ""
    for month in months:
        s += dicMonths[month] + ", "
    s = s[:-2]

    plotFrequency(retrieveMonths(dataDictionary(data), months), 50, s, filepath)


def customWordCloud(data, months, numWords, filepath):
    createWordCloud(retrieveMonths(dataDictionary(data), months), numWords, filepath)
