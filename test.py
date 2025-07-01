import random 

class_roster = ["Alassan", "Amauri", "Andrew", "Anerys"]

rand = input("Generate? y/n: ")

while rand != "n":
    print(random.choice(class_roster))
    rand = input("Generate? y/n: ")