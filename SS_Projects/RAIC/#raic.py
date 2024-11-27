from Pafez import rollprob, benfordise, benfordperc
from random import randint
from os import system as sys
from time import sleep


letts = list(" abcdefghijklmnopqrstuvwxyz.,:;!?'" + '"')

letcoun = []
for i in letts:
    letcoun.append(0)

letcoun.append(1)
letperc = []
for i in letcoun:
    t = sum(letcoun)
    letperc.append(i/t)
letcoun.pop()
letperc.pop()
    

words = []
wordcoun = []
wordperc = []
twc = 0
def upword(word):
    global twc, wordperc
    for i in range(len(words)):
        if word == words[i]:
            wordcoun[i] += 1
    if not word in words:
        words.append(word)
        wordcoun.append(1)
    twc += 1
    wordperc = []
    for i in wordcoun:
        wordperc.append(i/twc)

def genlet(prob):
    return letts[rollprob(letperc)-1]

def genransenl():
    msg = ""
    for i in range(randint(0,20)):
        l = rollprob(letperc)
        msg += letts[l-1]
        
    return msg

def genransent():
    msg = ""
    for i in range(randint(0,10)):
        r = rollprob(wordperc)
        
        if len(words) > 0:
            msg += words[r-1] + " "
        
    return msg
    
while True:
    inp = list(input().split())
    
    for i in inp:
        upword(i)
    
    out = genransent()
    
    print("C::",out)
        
    
