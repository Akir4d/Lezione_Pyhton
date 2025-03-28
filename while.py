i=0
while i < 5:
    i=i+1
    print(i) 

menu = ""
while menu != "basta":
    menu=input("cosa vuoi mangiare? (dimmi basta per terminare)")
    if menu == "pasta":
        print("con il pomodoro")
    elif menu == "lasagna":
        print("bianca?")
    elif menu == "orecchiette":
        print("con le cime di rapa?")
    else:
        print("pizza con l'ananas?")