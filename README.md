# Tweeter-Sentiment-Classifier
## Introduction
We are using synthetic (fake, semi-randomly generated) twitter data in a csv file named project_twitter_data.csv which has the text of a tweet, the number of retweets of that tweet, and the number of replies to that tweet. We have also words that express positive sentiment and negative sentiment, in the files positive_words.txt and negative_words.txt.
Using this information we are building a sentiment classifier, which will detect how positive or negative each tweet is. We will create a csv file, which contains columns for the Number of Retweets, Number of Replies, Positive Score (which is how many happy words are in the tweet), Negative Score (which is how many angry words are in the tweet), and the Net Score for each tweet. At the end we will produce a graph of the Net Score vs Number of Retweets.
### strip_Puntuation
A function called strip_punctuation which takes one parameter, a string which represents a word, and removes characters considered punctuation from everywhere in the word. 
### get_pos
Next, we define a function called get_pos which takes one parameter, a string which represents one or more sentences, and calculates how many words in the string are considered positive words. We are using the list, positive_words to determine what words will count as positive. The function will return a positive integer - how many occurrences there are of positive words in the text. 
### get_neg
Next, a function called get_neg which takes one parameter, a string which represents one or more sentences, and calculates how many words in the string are considered negative words. Using the list, negative_words to determine what words will count as negative. The function will return a positive integer - how many occurrences there are of negative words in the text.
### Calculation
Finally, using our previous functions and the fake generated twitter data we will build a sentiment classifier, which will detect how positive or negative each tweet is. and create a csv file called resulting_data.csv, which contains the Number of Retweets, Number of Replies, Positive Score (which is how many happy words are in the tweet), Negative Score (which is how many angry words are in the tweet), and the Net Score (how positive or negative the text is overall) for each tweet. Then using Matplotlib, we will produce a graph of the Net Score vs Number of Retweets.


