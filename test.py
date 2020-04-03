import numpy as np
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer() 

#doc = ['Give me a sentence', 'The cat is cute','The dog is ugly','Birds are the devil']

val = input("Give us your sentence: ")
pieces = val.split(".")
doc = []

for sections in pieces:
    if sections != "" and sections!= " ":
        doc.append(sections)
print(doc)

pos_scores = []
neu_scores = []
neg_scores = []
comp_scores = []


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

print(np.average(comp_scores)*100)
    