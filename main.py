# Import
from os import system, name
from time import sleep

# Define Variables and Functions
points = 0
print("Welcome to GuessTheLyrics")

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
def nextlevel():
    clear()
    print("You have", points, "points")

print("Level 1")
lv1 = str(input("Choose a song:\nOption 1: Bohemian Rhapsody\nOption 2: Wrecking Ball\n"))

game = True
while game:
    level1 = True
    while level1:
        if lv1 in ["1", "Bohemian Rhapsody", "Option 1"]:
            lv1a1 = str(input("What are the missing lyrics:\n'Mama, just ______ a man'?\n"))
            if lv1a1 in ["killed", "Killed", "KILLED", "killed.", "Killed."]:
                print("Correct!")
                points += 1
                level1 = False
                
            else:
                print("Incorrect.")
                level1 = False
                game = False
        elif lv1 in ["2", "Wrecking Ball", "Option 2"]:
            lv1a1 = str(input("What are the missing lyrics:\n'I came in ___ a ___.'?\n"))
            if lv1a1 in ["like wrecking", "like, wrecking", "likewrecking", "like. wrecking", "LIKE WRECKING", "LIKE, WRECKING", "like a wrecking", "like a wrecking."]:
                print("Correct!")
                points += 1
                level1 = False
        else:
            print("Invalid option, please try again.")
    level2 = True
    nextlevel()

    while level2:
        print("Working.")
        sleep(20)
        
print("Game Over. Your score was", points)
