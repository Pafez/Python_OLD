import androidhelper
import time

def write(x):
    return print(x)

def read():
    return input()

def say(x):
    self = androidhelper.Android()
    return self.ttsSpeak(x)

def show(x):
    self = androidhelper.Android()
    return self.makeToast(x)
    
def wait(x):
    return time.sleep(x)
