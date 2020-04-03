# Imports 

import numpy as np
import json
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer() 

# Get user input

val = input("Give us your sentence: ")
pieces = val.split(".")
doc = []

# Break up user input per sentence and populate doc array

for sections in pieces:
    if sections != "" and sections!= " ":
        doc.append(sections)
print(doc)

# Array setup for holding scores

pos_scores = []
neu_scores = []
neg_scores = []
comp_scores = []

# Populate above arrays with the scores per sentence

for sentence in doc:
    vs = analyzer.polarity_scores(sentence)
    
    pos_scores.append(vs["pos"])
    neu_scores.append(vs["neu"])
    neg_scores.append(vs["neg"])
    comp_scores.append(vs["compound"])

    print("{:-<65} {}".format(sentence, str(vs)))
    # print('pos',pos_scores)
    # print('neu', neu_scores)
    # print('neg',neg_scores)
    # print('comp', comp_scores)

# Setup dictionary
summary = {'pos': 0, 'neu': 0, 'neg': 0, 'comp': 0 }

# print(("%.2f" % (np.average(comp_scores)*10)))
# print(np.average(pos_scores)*100)
# print(np.average(neu_scores)*100)
# print(np.average(neg_scores)*100)

# Populate dictionary with average values

summary['pos'] = ("%.2f" % (np.average(pos_scores)*10)) 
summary['neu'] = ("%.2f" % (np.average(neu_scores)*10)) 
summary['neg'] = ("%.2f" % (np.average(neg_scores)*10)) 
summary['comp'] = ("%.2f" % (np.average(comp_scores)*10)) 

# JSONify dictionary

summary_json = json.dumps(summary)
print(summary_json)


