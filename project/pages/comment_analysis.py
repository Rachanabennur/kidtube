import nltk
import emoji
import re 
import statistics
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sid=SentimentIntensityAnalyzer()


def analysis(filtered_comments):
    positive = 0
    wpositive = 0
    spositive = 0
    negative = 0
    wnegative = 0
    snegative = 0
    neutral = 0
    track = []
    safe_comments=[]
    for comment in filtered_comments:
        i = sid.polarity_scores(comment)['compound']
        if (i == 0):  
                neutral += 1
                safe_comments.append(comment)
        elif (i > 0 and i <= 0.3):
            wpositive += 1
            safe_comments.append(comment)
        elif (i > 0.3 and i <= 0.6):
            positive += 1
            safe_comments.append(comment)
        elif (i > 0.6 and i <= 1):
            spositive += 1
            safe_comments.append(comment)
        elif (i > -0.3 and i <= 0):
            wnegative += 1
        elif (i > -0.6 and i <= -0.3):
            negative += 1
        elif (i > -1 and i <= -0.6):
            snegative += 1
        track.append(i)



    NoOfTerms = len(filtered_comments)


    positive = format(100 * float(positive) / float(NoOfTerms), '0.2f')
    wpositive = format(100 * float(wpositive) / float(NoOfTerms), '0.2f')
    spositive = format(100 * float(spositive) / float(NoOfTerms), '0.2f')
    negative = format(100 * float(negative) / float(NoOfTerms), '0.2f')
    wnegative = format(100 * float(wnegative) / float(NoOfTerms), '0.2f')
    snegative = format(100 * float(snegative) / float(NoOfTerms), '0.2f')
    neutral = format(100 * float(neutral) / float(NoOfTerms), '0.2f')



    Final_score = statistics.mean(track) 

    if Final_score>0:
        print("Using Vader Sentiment Analyzer: ")
        print("    Overall Reviews are Positive with Score "+ str(format(100 * Final_score , '0.2f')+"% \n"))
    elif Final_score<0:
        print("Using Vader Sentiment Analyzer: \n")
        print("Overall Reviews are Negative with Score "+ str(format(100 * Final_score , '0.2f')+"% \n"))
    else :
        print("Using Vader Sentiment Analyzer: \n")
        print("Overall Reviews are Moderate with Score "+ str(format(100 * Final_score , '0.2f')+"% \n"))


    print()
    print("Detailed Report: ")
    print(str(positive) + "% people thought it was positive")
    print(str(wpositive) + "% people thought it was weakly positive")
    print(str(spositive) + "% people thought it was strongly positive")
    print(str(negative) + "% people thought it was negative")
    print(str(wnegative) + "% people thought it was weakly negative")
    print(str(snegative) + "% people thought it was strongly negative")
    print(str(neutral) + "% people thought it was neutral")

    # from textblob import TextBlob

    # positive = 0
    # wpositive = 0
    # spositive = 0
    # negative = 0
    # wnegative = 0
    # snegative = 0
    # neutral = 0
    # track = []
    # for comment in filtered_comments:
    #     analysis = TextBlob(comment)
    #     i = analysis.sentiment.polarity
    #     if (i == 0):  
    #             neutral += 1
    #     elif (i > 0 and i <= 0.3):
    #         wpositive += 1
    #     elif (i > 0.3 and i <= 0.6):
    #         positive += 1
    #     elif (i > 0.6 and i <= 1):
    #         spositive += 1
    #     elif (i > -0.3 and i <= 0):
    #         wnegative += 1
    #     elif (i > -0.6 and i <= -0.3):
    #         negative += 1
    #     elif (i > -1 and i <= -0.6):
    #         snegative += 1
    #     track.append(i)



    # NoOfTerms = len(filtered_comments)


    # positive = format(100 * float(positive) / float(NoOfTerms), '0.2f')
    # wpositive = format(100 * float(wpositive) / float(NoOfTerms), '0.2f')
    # spositive = format(100 * float(spositive) / float(NoOfTerms), '0.2f')
    # negative = format(100 * float(negative) / float(NoOfTerms), '0.2f')
    # wnegative = format(100 * float(wnegative) / float(NoOfTerms), '0.2f')
    # snegative = format(100 * float(snegative) / float(NoOfTerms), '0.2f')
    # neutral = format(100 * float(neutral) / float(NoOfTerms), '0.2f')



    # Final_score = statistics.mean(track) 

    # if Final_score>0:
    #     print("Using TextBlob Sentiment Analyzer: ")
    #     print("    Overall Reviews are Positive with Score "+ str(format(100 * Final_score , '0.2f')+"% \n"))
    # elif Final_score<0:
    #     print("Using TextBlob Sentiment Analyzer: \n")
    #     print("Overall Reviews are Negative with Score "+ str(format(100 * Final_score , '0.2f')+"% \n"))
    # else :
    #     print("Using TextBlob Sentiment Analyzer: \n")
    #     print("Overall Reviews are Moderate with Score "+ str(format(100 * Final_score , '0.2f')+"% \n"))


    # print()
    # print("Detailed Report: ")
    # print(str(positive) + "% people thought it was positive")
    # print(str(wpositive) + "% people thought it was weakly positive")
    # print(str(spositive) + "% people thought it was strongly positive")
    # print(str(negative) + "% people thought it was negative")
    # print(str(wnegative) + "% people thought it was weakly negative")
    # print(str(snegative) + "% people thought it was strongly negative")
    # print(str(neutral) + "% people thought it was neutral")
    print(safe_comments)
    return(safe_comments)
