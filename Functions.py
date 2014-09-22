def mainmenu():
    firt = input("Do you want to start the game? [Type start if you want to start]").strip().lower()
    if firt == "start":
        print("GAMESTART")
        fun()
    else:
        print("WAAT")
        mainmenu()

def fun():
    di = input("Do you want to go right or left?").strip().lower()
    if di == "right":
        print("You go right.")
        fun()
    elif di == "left":
        print("You go left")
        fun()
    else:
        print("I do not understand")
        fun()

        




mainmenu()
