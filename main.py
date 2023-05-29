# What's The Lyric! V 0.0.1 Alpha
# Changelog
# - First version
# To-do
# - Finish first levels (1-10)
# - Add Music

# Import
from os import system, name
from time import sleep

# Define Variables and Functions
points = 0
level = 1

song1 = "Bohemian Rhapsody"  # wrong level, fix later
lyrics1 = "Mama, just ___ a man."
ans1 = ["killed", "Killed", "KILLED"]

song2 = "Wrecking Ball"
lyrics2 = "I came in ___ a ___ ___."
ans2 = ["like wrecking ball", "like a wrecking ball", "LIKE WRECKING BALL", "LIKE A WRECKING BALL", "Like wrecking ball", "Like Wrecking Ball", "like, wrecking, ball", "Like, Wrecking, Ball"]

song3 = "Let It Go"
lyrics3 = "Let it go, let it go, cant ___ it ___ anymore."
ans3 = ["Hold Back", "Hold back", "hold Back", "holdback", "HOLD BACK", "HOLD, BACK", "HOLDBACK", "hold it back."]

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def nextlevel():
    global level, points
    clear()
    print("You have", points, "points")

game = True
while game:
    level1 = True
    while level1:
        print("Level 1")
        lv1 = str(input("Choose a song:\nOption 1: Bohemian Rhapsody\nOption 2: Wrecking Ball\nOption 3: Let It Go\n"))
        if lv1 in ["1", "Bohemian Rhapsody", "Option 1"]:
            lv1a1 = str(input("What are the missing lyrics:\n'Mama, just ______ a man'?\n"))
            if lv1a1 in ["killed", "Killed", "KILLED", "killed.", "Killed."]:
                print("Correct!")
                points += 1
                level1 = False
                
            else:
                game = False # broken
        elif lv1 in ["2", "Wrecking Ball", "Option 2"]:
            lv1a1 = str(input("What are the missing lyrics:\n'I came in ___ a ___.'?\n"))
            if lv1a1 in ["like wrecking", "like, wrecking", "likewrecking", "like. wrecking", "LIKE WRECKING", "LIKE, WRECKING", "like a wrecking", "like a wrecking."]:
                print("Correct!")
                points += 1
                level1 = False
        elif lv1 in ["3", "Let It Go", "Let it go", "Let It Go", "let it go", "Option 3"]: # Level incomplete
            lv1a1 = str(input("What are the missing lyrics:\n'Let it go, let it go, cant ___ it ___ anymore.'?\n"))
            if lv1a1 in ["Hold Back", "Hold back", "hold Back", "holdback", "HOLD BACK", "HOLD, BACK", "HOLDBACK", "hold it back."]:
                print("Correct!")
                points += 1
                level1 = False
        else:
            print("Invalid option, please try again.")
            
    nextlevel()

    song1 = "Another One Bites The Dust"
    lyrics1 = "___ of ___ doorway the ___ ___."
    ans1 = ["out the bullets rip", "out of the doorway the bullets rip", "out, the, bullets, rip", "OUT THE BULLETS RIP", "Out the bullets rip", "Out, the, bullets, rip"]

    level2 = True
    while level2:
        print("Level 2")
        lv1 = input("Choose a song:\nOption 1: Another One Bites The Dust\nOption 2: Back In Black\nOption 3: We Didn't Start the Fire\n")
        if lv1 in ["1", "Another One Bites The Dust", "Option 1"]:
            lv1a1 = str(input("What are the missing lyrics:\n'___ of ___ doorway the ___ ___.'?\n"))
            if lv1a1 in ["out the bullets rip", "out of the doorway the bullets rip", "out, the, bullets, rip", "OUT THE BULLETS RIP", "Out the bullets rip", "Out, the, bullets, rip"]:
                print("Correct!")
                points += 1
                level1 = False
            else:
                game = False  # broken

        elif lv1 in ["2", "", "Option 2"]:
            lv1a1 = str(input("What are the missing lyrics:\n'LYRICS'?\n"))
            if lv1a1 in [""]:
                print("Correct!")
                points += 1
                level1 = False
        elif lv1 in ["3", "Let It Go", "Let it go", "Let It Go", "let it go", "Option 3"]: # Level incomplete
            lv1a1 = str(input("What are the missing lyrics:\n'Let it go, let it go, cant ___ it ___ anymore.'?\n"))
            if lv1a1 in ["Hold Back", "Hold back", "hold Back", "holdback", "HOLD BACK", "HOLD, BACK", "HOLDBACK", "hold it back."]:
                print("Correct!")
                points += 1
                level1 = False
        else:
            print("Invalid option, please try again.")

print("Game Over. Your score was", points)
