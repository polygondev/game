# What's The Lyric! V 0.0.1 Alpha
# Changelog
# - First version
# To-do
# - Finish first levels (1-10)
# - Add Music

# Import
from os import system, name

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
    level += 1
    print("You have", points, "points")


def level():
    global level, points
    levelselect = input("Choose a song:\nOption 1: " + song1 + "\nOption 2: " + song2 + "\nOption 3: " + song3 + "\n")
    if levelselect in ["1", song1, "Option 1"]:
        userans = input("What are the missing lyrics:\n'" + lyrics1 + "'?\n")
        if userans in ans1:
            print("Correct!")
            points += 1
            level_active = False
        else:
            level_active = False

    elif levelselect in ["2", song2, "Option 2"]:
        userans = input("What are the missing lyrics:\n'" + lyrics2 + "'?\n")
        if userans in ans2:
            print("Correct!")
            points += 1
            level_active = False
    elif levelselect in ["3", song3, "Let It Go", "Let it go", "let it go", "Option 3"]:  # Level incomplete
        userans = input("What are the missing lyrics:\n'" + lyrics3 + "'?\n")
        if userans in ans3:
            print("Correct!")
            points += 1
            level_active = False
    else:
        print("Invalid option, please try again.")


game = True
while game:
    level_active = True
    while level_active:
        level()
    nextlevel()

    song1 = "Another One Bites The Dust"
    lyrics1 = "___ of ___
