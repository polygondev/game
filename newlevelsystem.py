points = 0

def wrong():
    print("Incorrect. If your answer is correct, please add an issue to GitHub\nhttps://github.com/polygondev/game/issues")
    input("Press enter to quit game.")
    exit()
def correct():
    points += 1
    print("Correct! You have", points, "point(s)")
    level = False

song = input("Choose a song: \n1. Bohemian Rhapsody \n2. Wrecking Ball \n3. Let It Go")

level = True
while level:
    if song in ["1", "Bohemian Rhapsody"]: # Song one
        ans1 = input("What are the missing lyrics? 'Mama, just ___ a man.' ")
        if ans1 in ["killed", "Killed", "KILLED", "killed.", "Killed."]:
            correct()
        else:
            wrong()

    elif song in ["2", "Wrecking Ball"]: # Song two
        ans1 = input("What are the missing lyrics? 'I came in ___ a ___.' ")
        if ans1 in ["like wrecking", "like, wrecking", "likewrecking", "like. wrecking", "LIKE WRECKING", "LIKE, WRECKING", "like a wrecking", "like a wrecking."]:
            correct()
        else:
            wrong()
            
    elif song in ["3", "Let It Go"]: # Song three
        ans1 = input("What are the missing lyrics? 'Let it go, let it go, cant ___ it ___ anymore.' ")
        if ans1 in ["Hold Back", "Hold back", "hold Back", "holdback", "HOLD BACK", "HOLD, BACK", "HOLDBACK", "hold it back."]:
            correct()

        else:
            wrong()

song = input("Choose a song: \n1. Back In Black \n2. We Didn't Start the Fire \n3. Another One Bites The Dust")

level = True
while level:
    if song in ["1", "Back In Black"]: # Song one
        ans1 = input("What are the missing lyrics? 'I ___ the ___. I've ___ to long, I'm ___ to be ___.' ")
        if ans1 in ["NOT DONE"]:
            correct()
        else:
            wrong()

    elif song in ["2", "We Didn't Start The Fire", "we didn't start the fire"]: # Song two
        ans1 = input("What are the missing lyrics? 'It ___ always ___ since ___ ___ was turning.' ")
        if ans1 in ["was burning the world", "Was Burning The World", "WAS BURNING THE WORLD", "wasburningtheworld", "was, burning, the, world."]:
            correct()
        else:
            wrong()
            
    elif song in ["3", "Let It Go"]: # Song three
        ans1 = input("What are the missing lyrics? 'Let it go, let it go, cant ___ it ___ anymore.' ")
        if ans1 in ["Hold Back", "Hold back", "hold Back", "holdback", "HOLD BACK", "HOLD, BACK", "HOLDBACK", "hold it back."]:
            correct()

        else:
            wrong() #yo callum me sick 