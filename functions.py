import os
import time
def pause(def_time):
    time.sleep(def_time)
def reverse_text(text_input):
    size=len(text_input)
    i=size-1
    while i>=0:
        print(f"{text_input[i]}", end="", flush= True)
        pause(0.05)
        i-=1
def clean():
    os.system("cls")