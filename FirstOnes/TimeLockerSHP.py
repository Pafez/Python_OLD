import time
import androidhelper
droid = androidhelper.Android()
r = time.strftime("%I%M")
t = 0

print("Enter the code in 3 turns or Goodbye...")
droid.ttsSpeak("Enter the code in 3 turns or,, Goodbye...")
while 1 == 1:
    s = input("")
    if s == r:
        print("Welcome, sir.")
        droid.ttsSpeak("Welcome, sir.")
    else:
        print("Access denied, failed attempt",t+1)
        droid.ttsSpeak("Access denied")
        t = t + 1
        if t == 3:
            droid.ttsSpeak("Goodbye")
            break
