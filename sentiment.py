# Uses python3
##################################################
## For detail refer README.md in the main folder
##################################################
## GNU General Public License v3.0
##################################################
## Author: ANURAG GARG
## Copyright: Copyright 2020, Tweeter Sentiment Classifer.

## Credits: University of Michigan and Coursera
# Python 3 Specialization.

## License: GNU GPL v3.0
## Version: 1.1.0
## Mmaintainer: ANURAG GARG
## Email: mranuraggarg@yahoo.com
## Status: stable
####################################################################################################
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']


def strip_punctuation(word):
    for punct in punctuation_chars:
        word = word.replace(punct, '')
    return word


def get_pos(string):
    string_lst = []
    for word in string.split():
        string_lst.append(strip_punctuation(word.lower()))
    string_lst = Counter(string_lst)
    positive_count = [string_lst[p_word] if p_word in string_lst \
                          else 0 for p_word in positive_words]
    return sum(positive_count)


def get_neg(string):
    string_lst = []
    for word in string.split():
        string_lst.append(strip_punctuation(word.lower()))
    string_lst = Counter(string_lst)
    negative_count = [string_lst[n_word] if n_word in string_lst \
                          else 0 for n_word in negative_words]
    return sum(negative_count)


# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

###### Beginning of Twitter Data analysis ######

if __name__ == '__main__':
    with open("project_twitter_data.csv") as tweet_file:
        iteration = 0
        with open("resulting_data.csv", "w") as res_file:
            res_file.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
            res_file.write('\n')
            tweet_file.readline()
            for line in tweet_file:
                lst_comma = line.strip().split(',')
                tweet_text = lst_comma[0]
                pos_count = get_pos(tweet_text)
                neg_count = get_neg(tweet_text)
                retweet_count = lst_comma[1]
                reply_count = lst_comma[2]
                net_score = pos_count - neg_count
                row = "{},{},{},{},{}".format(retweet_count,
                                              reply_count,
                                              pos_count,
                                              neg_count,
                                              net_score)
                res_file.write(row)
                res_file.write('\n')

                ## End of for loop ##

    ###### Plotting Twitter data ######

    tweet_df = pd.read_csv("resulting_data.csv")
    tweet_df.plot.scatter(x=" Net Score",
                          y="Number of Retweets",
                          )
    plt.xlabel('Tweets\' Net score')
    plt.ylabel("Number of Retweets")
    plt.title("Sentiment Classifier Graph")
    plt.minorticks_on()
    plt.savefig('Sentiment Classifier-Graph.jpeg', dpi=300)

###### End of Twitter Data analysis ######
