import random ,words ,os,time

max = print("coded by max23 \nenjoy it =)\nsubscribe philolearn")
time.sleep(1)

random.seed()


health = 6
choosedword=[]
guessedword = []
def play():

    def sendresult():
        for x in range(len(choosedword)):
            print(f"{choosedword[x]}",end="")
        print("\nwell done! you won!")
        again()

    def printresult():
        for x in range(len(choosedword)):
            print(f"{guessedword[x]}", end=" ") 

    word = random.choice(words.words)
    for x in word:
        choosedword.append(x)
    for x in range(len(choosedword)):
        guessedword.append("_")
    for x in range(len(choosedword)):
        print(f"{guessedword[x]}", end=" ")

    global health

    def numberhealth():
        global health
        health -= 1
        if health == 0:
            for x in range(len(choosedword)):
                print(f"{choosedword[x]}",end="")
            print("\nGame Over!")
            again()
        
       

    while health>0:
        print(f"\nyour chance:{health}")
        input1 = input("Enther your letter:")
        k = True
        for x in range(len(choosedword)):
            if input1 == choosedword[x]:
                guessedword.pop(x)
                guessedword.insert(x,input1)
                k = False
                q ="_"
                if q not in guessedword:
                    health = 0
                    sendresult()
        while k:
            numberhealth()
            break
        printresult()
clears = lambda: os.system('cls')
def again():
    global health
    input2 = input("do you want play again?(yes/no)")
    if input2 == "yes":
        choosedword.clear()
        guessedword.clear()
        clears()
        health = 6
        play()
    else:
        quit

play()