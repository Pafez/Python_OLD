from os import system
from time import sleep
import html
for hour in range(24):
    for minute in range(60):
        for second in range(60):
            clock = str(hour) + ":" + str(minute) + ":" + str(second)
            system("clear")
            print(clock)
            sleep(1)

