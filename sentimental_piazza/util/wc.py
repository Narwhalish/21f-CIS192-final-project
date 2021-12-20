data = [
    [
        12,
        "Hi all, I had a chance to think about what topics to include for the finals. Having 25% of the grade dependent on just the last third of the course seemed a little disproportionate. So, what we're going to do is the following: 1) The emphasis of the finals will be on topics covered in the last 1/3 of the course -- i.e., P, NP, NP-completeness and space complexity. 2) There will be either one or two questions on undecidability / non recognizability. I feel you anyway need to be thorough with the concept of reductions in context of computability if you want to understand it in context of complexity. So, hopefully, this will avoid putting disproportionate weight on any one topic while still avoiding a cumulative finals. Finally, while I won't ask questions directly related to finite automata (as in show, some language X is regular), as you have seen, many questions in space complexity involve finite automata.I will be happy to discuss this in more detail.  ",
    ],
    [
        9,
        "Hi all, Problem 2 in Homework 1 asks students to design a DFA. If you wish to do it online, we recommend the following tool: [http://madebyevan.com/fsm/](http://madebyevan.com/fsm/) Instructions for its use are at the bottom, but post on Piazza if you have any issues with it. Additionally, feel free to use a different tool if you have one. Future homeworks may also ask you to create FSMs, and this website should be helpful for that as well. Note that a common issue occurs for those using Macs: when you would like to delete a state or an edge, you must press `fn + delete` instead of just `delete`.  ",
    ],
    [
        10,
        '  # OHQ and Office Hour Etiquette  Hi all,  The CIS 262 staff would like to clarify some expectations for OHQ and office hours for students to refer to as they enter the queue.  1) **Students must disable their waiting room before entering the queue.** You can read about the details [here](https://support.zoom.us/hc/en- us/articles/115000332726-Waiting-Room), but when you have a room up, it\'s basically just clicking Security -> Enable Meeting Room to enable/disable it. **If a TA comes into a room with a waiting room, they will leave** (pending a minute or two of waiting). Most of the time, there are simply too many people in the queue to justify staying in a student\'s wait room: we hope you understand.  2) **Please disable the passcode on your room. If your room must have a password, put it in the question description.** It looks like only people who are using their pennkey@upenn.edu (instead of pennkey@<seas/sas/etc.>upenn.edu) for their Zoom accounts (and have a Zoom license granted by the University) have the option to turn this off. If you do not have a licensed version, you may not be able to turn this off in which case you can find the passcode in Meetings -> Show Meeting Invitation.  3) **Regrade requests cannot not be verified in office hours.** You are more than welcome to come into office hours to ask about concepts you didn\'t understand in the homework, and express any confusion regarding why you lost points on an assignment. However, the TA cannot give you back the points in office hours, nor can they make any guarantees about whether or not you deserve the points back. Those conversations can only take place in Gradescope regrade requests.  4) **Please write descriptive comments on OHQ**. The TAs might be more prepared to answer your question if you provide a descriptive question. Instead of writing "Problem 2" or "HW1", please try to take a few seconds to write out "Confused about how to prove a DFA is correct for question 2" or "Need help generalizing my proof for question 1a".  5) While you can have your collaborator in your Zoom room, you cannot record your virtual OH sessions.  And of course, the TAs are not permitted to give students homework answers in office hours—we\'re there to help you learn the material, and making sure you can answer the homework problems yourselves is a big part of that!  **#pin**  ',
    ],
    [8, "#pin  "],
    [
        11,
        "Hi all, It seems like that there is some confusion concerning HW8. 1\\. In Q1, several students have asked whether it is ok to have a running time of $$n^k$$. No, it is not. The language L' consists of those strings which can be written as a concatenation of k different strings from $$L$$ for any $$k$$. I had hoped that this is clear but I have reworded the question to make sure this is absolutely clear now. Even if you have assumed that $$k$$ is a parameter in the problem definition, I would be perfectly fine the solution as long as it is polynomial time -- i.e., should run in time polynomial in both $$n$$ and $$ \\log k$$. 2\\. In Q2, the input is a concatenation of n different integers. The input size will depend on how many bits you spend representing each of these numbers. In particular, think about the following: suppose each number is at most $$2^k$$. How many bits do you then require to represent $$n$$ such numbers?? Note that even to represent one number, you require $$k$$ bits.  ",
    ],
    [10, "  "],
    [
        10,
        "  We just released the Midterm 1 grades on gradescope. The gradecope only contains your score and some comments about your exam. If you would like the physical copy of your exam, please come to my OH (tomorrow 6-7) and Hannah's (tomorrow 7-8) both of which will be in 512 Levine, or email Professor De for an appointment for an alternate time to pick up your exam.  We will allow you to file regrade requests, with this Professor De will regrade your entire exam. You can do this by emailing him and bringing in your picked up exam.  If any of you have question or concerns about dropping the class please reach out to Professor De or the Head Ta's. Please note that we emphasize your performance as the class goes on, thus it is very likely that you can succeed in this course despite a low Midterm 1 grade.  Overall, good job everyone. We were very pleased with the scores on Midterm 1.  ",
    ],
    [
        10,
        "  ****NOTE - this schedule is out of date. Please refer to Canvas for the current OH schedule.**  ****  **For the time being all OH will be online on OHQ.**  You should be able to add yourself to the course on ohq.io by just searching for CIS 262. Please email me (pscanlan@seas.upenn.edu) if you have any issues.  The homework will be released shortly to be due next Monday (9/13).  The following is our office hours schedule to begin this TUESDAY (9/7):  **Monday:**  Professor De - 3-4  Paula - 6-7  Hannah - 7-8  **Tuesday:**  Jaume - 4-5  Alan - 7-8  **Wednesday:**  Alina 1:30-2:30  **Thursday:**  Ethan - 2-3  Raunaq - 4-5  **Friday:**  Akshat - 2-3  Aakash - 3-4  **Saturday:**  Sumi - 1-2  **Sunday:**  Brandy - 10:30 - 11:30  Andrew - 4-5  Acelyn - 6-7  ",
    ],
    [
        12,
        "  Hi all,  I will have a review session tonight at 10 pm. I will discuss the answers to the last two questions.  In addition, I will have a review session tomorrow from 2-3 pm and day after from 10:30 am - 11:30 am.  Anindya  ",
    ],
    [
        12,
        "  I know we have seen a lot of NP-complete problems, but I wanted to check that this is a somewhat complete list and the correct reasonings as to why:  SAT is NP-complete (by original Cook's Theorem)  INVALID is NP-complete (by SAT <p INVALID)  INDEPSET is NP-complete (by ? )  CLIQUE is NP-complete (by ? )  CNF-SAT is NP-complete (by SAT <p CNF-SAT)  3SAT is NP-complete (by CNF-SAT <p 3SAT)  For independent set and clique, I know there are multiple ways to prove they are NP-complete (reductions from other languages), but what is the easiest/what we went over in class?  ",
    ],
    [
        12,
        "  Hey, like on the previous exam can we get a rough estimate as to how the practice final compares to the real final difficulty wise?  ",
    ],
    [
        12,
        "  What is the difference between/relation between CoNP and EXPTIME? Is it just that all languages in CoNP are in EXPTIME, but not vice versa?  ",
    ],
    [
        12,
        "  Hi all,  Apologies for the late notice, but something important has come up and will conflict with my scheduled OH for today @ 4pm today.  I will move my OH to later tonight @8pm, still on Zoom. Let me know if there is a dissenting opinion to this suggested time; I am happy to schedule around getting the most people helped.  Cheers!  ",
    ],
    [12, "  Is the exam on gradescope or a PDF that we upload images on canvas?  "],
    [
        12,
        "  Can someone briefly explain why the algorithm for CLIQUE on slide 29 from lecture 18 has runtime O(n^2 2^n)? Thank you  ",
    ],
    [12, "  "],
    [
        12,
        "  Posted [Note_Dec_16,_2021.pdf](/redirect/s3?bucket=uploads&prefix=paste%2Fjr8geg4vix245v%2Fbdaa0c007d861eb6cd68bc2bc44c87f21e445e3eeb3a9c1b8813e47352c5bd9a%2FNote_Dec_16%2C_2021.pdf)  ",
    ],
    [12, "Title  "],
    [
        12,
        "  Hi everyone! I will need to move my OH this Sunday to today at 5PM instead.  Good luck with studying for the finals!       ",
    ],
    [
        12,
        "  hello, for the practice finals questions referenced on note @952, where could i find the solutions to the questions?  thanks!  ",
    ],
    [
        12,
        "  From review session (12/16) is here:  <https://upenn.zoom.us/rec/share/NGf1t_30d_Z91vOoeijZFiYwVAamVR0jdd3nGI- GSm77-EJ0zp0lme_s0w5vHpqi.-vPq9rTdDnTEhHSf> Passcode: 25XX1E=v  Please do go over the video.  ",
    ],
    [
        12,
        "Why do we require the guess to be polynomial in size of the input? It makes sense to have as a constraint but if it's not polynomial, wouldn't the verification be exponential anyway? Why is this an independent requirement?  ",
    ],
    [
        12,
        "  Unfortunately I have something conflicting with my office hours on Friday from 2-3pm, so it will be cancelled.  If you have any questions feel free to email me.  ",
    ],
    [
        12,
        "  Hi all,  I had planned to host the review session today but something has come up. So, I will host the online review session tomorrow from 3-4 pm. I have now posted all the questions I wanted on the overleaf link. If we're not able to finish discussing all the questions, we will do one more on Friday.  Also, if you have any other questions (other than the ones in the practice finals), please do feel free to discuss those in the review session. I am happy to host more of these but last time, there were only two students. So, I am reluctant to have more without some expression of interest.  Thanks,  Anindya  P. S. Do fill the course evaluations.  We're meeting here : https://upenn.zoom.us/my/anindyade  ",
    ],
    [12, "  ^  "],
    [12, "  Just to be absolutely sure, the final is on the 22nd right?  "],
    [
        12,
        "  Hi, I am moving my office hours this week to Thursday 12/16 from 3-4pm. I will still have my normal Tuesday OH on 12/21.  ",
    ],
    [
        12,
        "Hi all, I'm at a research conference today and won't be able to make my normally scheduled office hours today at 7-8 PM. I'll still hold office hours on 12/21 for any questions about the course material before the final. Sorry for the inconvenience.  ",
    ],
    [12, "^  "],
    [
        12,
        "  <https://upenn.zoom.us/rec/share/gYxxHCeIh4sRv3OApHsYgJhsEQL3m7E223IbFPC9fqzZT_gAhnEgUXaDwgdlkMcd.jOtWk934mIqEnGlV> Passcode: UUJY=3=w  The notes from the review session are here -- [Note_Dec_13,_2021.pdf](/redirect/s3?bucket=uploads&prefix=paste%2Fjr8geg4vix245v%2F6685ad474c19a553c6b3f6da56844805fadd54c61cff2caa6221cefda235dca6%2FNote_Dec_13%2C_2021.pdf)  ",
    ],
    [
        12,
        "  Hi all,  OH tonight at 6 (as well as the 7pm OH) will be on OHQ. Come by if you have any questions!  ",
    ],
    [
        12,
        "  Hi all,  I will be hosting a review session today (instead of the usual OH) from 3:00 -- 4:00 pm. It will be online and recorded. I doubt we will be able to do everything I want to cover. So, we will have one more in a couple of days.  Anindya  ",
    ],
    [
        12,
        "  Are there Professor office hours today at 3? Are they in person or online if so?  ",
    ],
    [12, "  When will the review session be?  "],
    [
        12,
        "  Hi all,  This is a partial list of questions for the practice finals. More will put on this [link](https://www.overleaf.com/read/phssrnmmqttg) in days to come.  Anindya  P. S. Please do try to fill in your CETS evaluation.  ",
    ],
    [
        12,
        "Apologies for the late notice—I won't be able to make my 3 PM OH today. Just for today, I’ll be hosting OH from 5-6 PM.  ",
    ],
    [12, "Or should we rewrite the algorithm??  "],
    [12, "  "],
    [12, "given G and k it checks if there exists a clique of size k right?  "],
    [12, "can generating random strings take PSPACE?  "],
    [
        12,
        "For PSPACE questions, should we be creating algorithm, proving correctness, proving pspace?  ",
    ],
    [
        12,
        "How did we get O(2nlogn) for the size of the input? Why does it have to be poly(kn)?  ",
    ],
    [
        12,
        "  In post @915, the professor gave an example proof of proving something is in PSPACE. Is the depth/detail in this example, the same as what we are expected to have in our homework 10 proofs? Is the level of depth shown in the example proof equivalent to that which we need in our homework assignment?  Thanks!  ",
    ],
    [
        12,
        "  As announced in the lecture yesterday, there is no recitation today (Dec 8).  There is a lecture tomorrow, Dec 9.  ",
    ],
    [12, "is there recitation today?  "],
    [
        12,
        "  When will the review session be for the exam? I am trying to figure out my schedule so any information on when this will be happening would be helpful, thank you  ",
    ],
    [
        12,
        "  If we make an algorithm for Q1, are these statements sufficient to prove for the POC:  If the algorithm accepts, the input is in MAX_CLIQUE  If an input is in MAX_CLIQUE, the algorithm accepts  I am just confirming that my iff understanding for the POC is correct.  Thank you  ",
    ],
    [
        12,
        "  Can we assume that CLIQUE is in PSPACE, or should we provide a proof for that?  ",
    ],
    [
        12,
        "Hello all,      I am moving my OH this week. Given the deadline, I’ll move the time to Thursday 3-4.  ",
    ],
    [
        12,
        "  Please see this recording from last night OH. I would strongly suggest doing this before tomorrow's lecture when we prove NPSPACE = PSPACE.  Long story short, while in tomorrow's lecture, we will show that NPSPACE = PSPACE, Q2 provides an application of this powerful theorem.     <https://upenn.zoom.us/rec/share/6eiN6dcWFTq1DvQllfk1mH7LqvZP0rYLAsCYK9mDUphnkPxkZrSaZ2XVVv6uqmeX.nZLwEkb6Q2Ao6vXD> Passcode: F6?b=9&3  ",
    ],
]
# install matplotlib, ntlk and WordCloud with 'pip3 install matplotlib', 'pip3 install nltk' & 'pip3 install Wordcloud'


import matplotlib.pyplot as plt
import nltk
from wordcloud import WordCloud

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
    f.close()
    return content_list


def createWordCloud(words, numWords):
    filtered_words = nltkfilter(words)
    plt.figure()
    wc = WordCloud(max_font_size=45, max_words=numWords, background_color="white")
    wordcloud_jan = wc.generate_from_text(" ".join(filtered_words))
    plt.imshow(wordcloud_jan, interpolation="bilinear")
    plt.axis("off")
    plt.show()


def plotFrequency(words, numWords, myTitle):
    filtered_words = nltkfilter(words)
    plt.figure()
    freq_dist = nltk.FreqDist(filtered_words)
    freq_dist.plot(numWords, cumulative=False, title=myTitle)


def customPlotFreq(data, months):
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

    plotFrequency(retrieveMonths(dataDictionary(data), months), 50, s)


def customWordCloud(data, months, numWords):
    createWordCloud(retrieveMonths(dataDictionary(data), months), 100)


customPlotFreq(data, [9, 12])
