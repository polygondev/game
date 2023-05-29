# What's The Lyric! V 0.0.1 Alpha
# Changelog
# - First version
# To-do
# - Finish first levels (1-10)
# - Add Music
# 

# Import
from os import system, name
from time import sleep

# Define Variables and Functions
points = 0
level = 1

song1 = "Bohemian Rhapsody" #wrong level, fix later
lyrics1 = "___ of ___ doorway the ___ ___."
ans1 = "out the bullets rip", "out of the doorway the bullets rip", "out, the, bullets, rip", "OUT THE BULLETS RIP", "Out the bullets rip", "Out, the, bullets, rip"

song2 = "Wrecking Ball"
lyrics2 = "I came in ___ a ___ ___."
ans2 = "like wrecking ball", "like a wrecking ball", "LIKE WRECKING BALL", "LIKE A WRECKING BALL", "Like wrecking ball", "Like Wrecking Ball", "like, wrecking, ball", "Like, Wrecking, Ball"

song3 = "3", "Let It Go", "Let it go", "Let It Go", "let it go", "Option 3"
lyrics3 = "Let it go, let it go, cant ___ it ___ anymore."
ans3 = "Hold Back", "Hold back", "hold Back", "holdback", "HOLD BACK", "HOLD, BACK", "HOLDBACK", "hold it back."



def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
def nextlevel():
    clear()
    level += 1
    print("You have", points, "points")
def level():
    levelselect = input("Choose a song:\nOption 1: ", song1, "\nOption 2: ", song2, "\nOption 3: ",song3 ,"\n")
    if levelselect in ["1", song1, "Option 1"]:
            userans = input("What are the missing lyrics:\n'", lyrics1,"'?\n")
            
            if userans in ans1:
                print("Correct!")
                points += 1
                level = False
            else:
                level = False 
        
    elif levelselect in ["2", song2, "Option 2"]:
        userans = input("What are the missing lyrics:\n'", lyrics2,"'?\n")
        
        if userans in ans2:
            print("Correct!")
            points += 1
            level = False
    elif levelselect in ["3", "Let It Go", "Let it go", "Let It Go", "let it go", "Option 3"]: # Level incomplete
        userans = input("What are the missing lyrics:\n'", lyrics3,"'?\n")
        
        if userans in ans3:
            print("Correct!")
            points += 1
            level = False
    else:
        print("Invalid option, please try again.")

game = True
while game:
    level1 = True
    while level:
        level()
    nextlevel()
    level2 = True
    while level2:
        print("Level 2")
        lv1 = str(input("Choose a song:\nOption 1: Another One Bites The Dust\nOption 2: Back In Black\nOption 3: We Didn't Start the Fire\n"))
        if lv1 in ["1", "Another One Bites The Dust", "Option 1"]:
            userans = str(input("What are the missing lyrics:\n'___ of ___ doorway the ___ ___.'?\n"))
            if userans in ["out the bullets rip", "out of the doorway the bullets rip", "out, the, bullets, rip", "OUT THE BULLETS RIP", "Out the bullets rip", "Out, the, bullets, rip"]:
                print("Correct!")
                points += 1
                level1 = False
                
            else:
                game = False # broken
        
        elif lv1 in ["2", "", "Option 2"]:
            userans = str(input("What are the missing lyrics:\n'LYRICS'?\n"))
            if userans in [""]:
                print("Correct!")
                points += 1
                level1 = False
        elif lv1 in ["3", "Let It Go", "Let it go", "Let It Go", "let it go", "Option 3"]: # Level incomplete
            userans = str(input("What are the missing lyrics:\n'Let it go, let it go, cant ___ it ___ anymore.'?\n"))
            if userans in ["Hold Back", "Hold back", "hold Back", "holdback", "HOLD BACK", "HOLD, BACK", "HOLDBACK", "hold it back."]:
                print("Correct!")
                points += 1
                level1 = False
        else:
            print("Invalid option, please try again.")
        
print("Game Over. Your score was", points)
