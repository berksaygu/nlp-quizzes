# Hasan Berk Saygu - 12.11.2022

import spacy;
import tensorflow as tf;
nlp = spacy.load('en_core_web_sm')

# Question 1: Create a Doc object from the file owlcreek.txt 
f = open(r'C:\Users\berks\Desktop\nlp\owlcreek.txt','r')
fileRead = f.read()
f.close(); 
doc1 = nlp(fileRead)

# Question 2: How many tokens are contained in the file?  
print(len(doc1))

# Question 3: How many sentences are contained in the file?
sents = [sent for sent in doc1.sents]
print(len(sents))

# Question 4: Print the second sentence in the document.
print(sents[1].text)

# Question 5: For each token in the sentence above,print its text,
#             POS tag, dep tag and lemma and have values line up in columns in the print output.
def printToken(sent):
    for token in sent:
        print(f'{token.text:{12}} {token.pos_:{6}} {token.dep_:{10}} {token.lemma_}')
printToken(sents[1])

# Question 6: Write a matcher called 'Swimming' that finds both occurrences of the phrase "swimming vigorously" in the text. 
#             You should include an 'IS_SPACE': True pattern between the two words!
from spacy.matcher import Matcher
matcher = Matcher(nlp.vocab)
pattern1 = [{'LOWER': 'swimming'}, {'IS_SPACE':True }, {'LOWER': 'vigorously'} ]
matcher.add('Swimming', [pattern1])

found_matches = matcher(doc1)
print(found_matches)

# Question 7: Print the text surrounding each found match.
for sent in sents:
    if found_matches[0][1] < sent.end:
        print(sent)
        break
for sent in sents:
    if found_matches[1][1] < sent.end:
        print(sent)
        break
    