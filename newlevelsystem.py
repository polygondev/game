points = 0

def wrong():
    print("Incorrect. If your answer is correct, please add an issue to GitHub\nhttps://github.com/polygondev/game/issues")
    input("Press enter to quit game.")
    exit()

song = input("Choose a song: \n1. Bohemian Rhapsody \n2. Wrecking Ball \n3. Let It Go")
if song in ["1", "Bohemian Rhapsody"]: # Song one
    ans1 = input("What are the missing lyrics? 'Mama, just ___ a man.' ")
    if ans1 in ["killed", "Killed", "KILLED", "killed.", "Killed."]:
        points += 1
        print("Correct! You have", points, "point(s)")
    else:
        wrong()

elif song in ["2", "Wrecking Ball"]: # Song two
    ans1 = input("What are the missing lyrics? 'I came in ___ a ___.' ")
    if ans1 in ["like wrecking", "like, wrecking", "likewrecking", "like. wrecking", "LIKE WRECKING", "LIKE, WRECKING", "like a wrecking", "like a wrecking."]:
        points += 1
        print("Correct! You have", points, "point(s)")
    else:
        wrong()
        
elif song in ["3", "Let It Go"]: # Song three
    ans1 = input("What are the missing lyrics? 'Let it go, let it go, cant ___ it ___ anymore.' ")
    if ans1 in ["Hold Back", "Hold back", "hold Back", "holdback", "HOLD BACK", "HOLD, BACK", "HOLDBACK", "hold it back."]:
        points += 1
        print("Correct! You have", points, "point(s)")
    else:
        wrong()