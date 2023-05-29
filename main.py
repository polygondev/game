import os
 
points = 0
print("Welcome to GuessTheLyrics")
name = input("What is your name")
print("Hello", name)

input("Press the Enter key to continue: ")

print("Level 1")
print("Use the number until we introduce text support")
lv1 = int(input("Choose a song:\nOption 1: Bohemian Rhapsody\nOption 2: Wrecking Ball"))

if lv1 in [1, "Bohemian Rhapsody", "Option 1"]:
    lv1s1 = input(("Guess the missing lyrics:\nMama, just ______ a man"))
    if lv1s1 == "killed":
        print("correct")

if lv1 in [2, "Wreakingball", "Option 2"]:
    lv1s1 = input(("Guess the missing lyrics:\nI came in ___ a ___"))
    if lv1s1 == "like wreakingball":
        print("correct")