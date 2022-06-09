import random
tday = datetime.date.today()
print(tday)
cocktail = ["old fashioned","mojito","pina colada","rum punch"]
winewine = ["red","rose","white"]

print("Tell me your age, I will guess your favourite alcohol?")

round = 0

round += 1
while True:
    age = int(input())

    if age < 21:
        print("WARNING,you are not supposed to drink alcohol")
        time.sleep(1)
        print("time to go home,kid")
        break
    elif age == 21:
        print("Alright, you got right to drink now, you drink all kinds of liquid")
        break
    elif age > 21 and age < 30:
        print("Cocktails, am I right?Looks fancy and tastes good")
        time.sleep(3)
        print("What is your favourite cocktails?", (random.choice(cocktail)),"?")
        if input() == 'mojito':
            print("you got nice taste")
        else:
            print("??????????????????????refuse to communicate")
        break
    elif age >=31 and age < 40:
        print("Romantic wine, life winner")
        time.sleep(3)
        print("Which type of wine do you like best?", (random.choice(winewine)),"?")
        if input() == 'red':
            print("that's a nice choice!")
        else:
            print("You are not gentleman~")
        break
    elif age >=40 and age < 50:
        print("Beer. Lying on the couch,watch ball games,chilling at home")
        time.sleep(3)
        print("Do you like Pale Ale? or Maybe bitter?")
        input()
        print("I totally agree with you~")
        break
    elif age >=50 and age < 100:
        print("hard liquid,be careful yo.let me know, I help you call 911!")
        time.sleep(3)
        print("Which hard liquid do you prefer? scotch or rum")
        input()
        print("Maybe you are right :)")
        break
    elif age >=100:
        print("no way you still alive, stop joking,bye")
        time.sleep(3)
        print("Come on, tell me your real age")
