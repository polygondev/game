import os
 
points = 0
print("Welcome to GuessTheLyrics")
name = input("What is your name?")
print("Hello", name)

input("Press the Enter key to continue: ")

print("Level 1")
print("Use the number until we introduce text support")
lv1 = int(input("Choose a song:\nOption 1: Bohemian Rhapsody\nOption 2: Wrecking Ball"))

if lv1 == 1:
    lv1s1 = str(("Guess the missing lyrics:\nMama, just ______ a man"))
else:
    print()