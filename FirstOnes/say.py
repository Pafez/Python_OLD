from androidhelper import Android
from os import system as sys

def say(n):
    an = Android()
    return an.ttsSpeak(n)

while False:
    j = input()
    say(j)
    sys("clear")
