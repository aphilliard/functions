# make breakfast
import sys
from time import sleep
from random import choice

spices_list = ("pepper", "paprika", "nutmeg", "mace", "clove", "ginger", "cinnamon")
meats_list = ("chicken", "pork", "beef", "turkey")
cook_eggs = ("fried", "scrambled", "over-easy", "poached")

def sausage_machine(m, s):
    print(f"Here is your {m} sausage made with fresh {s}!")
    
def kicked_out():
    print("You disgust me! Get out of here before I call the cops!")
    raise SystemExit

def order_eggs():
    print("Welcome to Hank's Down Home Diner! We serve eggs and sausage here.\n")
    global eggs
    global cook_style
    while True:
        try:
            eggs = int(input("How many eggs do you want? "))
            if eggs < 1:
                print("How about just one egg, then? You don't have to eat it.")
                eggs = 1
        except (ValueError):
            print("I need a number, honey.")
            continue
        else:
            break            
    
    if eggs > 4:
        print("That's a lot of eggs, but who am I to judge?\n")

    if eggs > 1:
        cook_style = ""
        while cook_style not in cook_eggs:
            cook_style = input("How do you want those eggs? ")
            if cook_style not in cook_eggs:
                print("I didn't catch that. These are your options: fried, over-easy, scrambled or poached.")
        print(f"You want {eggs} {cook_style} eggs.\n")        
        
    else:
        cook_style = ""
        while cook_style not in cook_eggs:
            cook_style = input("How do you want that egg? ")
            if cook_style not in cook_eggs:
                print("I didn't catch that. These are your options: fried, over-easy, scrambled or poached.")
        print(f"You want one {cook_style} egg.\n")

def order_sausage():
    print("Okay, now let's make some sausage!")
    meat = ""
    while meat not in meats_list:
        meat = input("What kind of meat? ").lower()
        if meat in ("human", "you", "person", "man", "dog"):
            kicked_out()
        if meat not in meats_list:
            print(f"I'm afraid we don't have that. {choice(meats_list).capitalize()} is pretty popular.")
    print(f"{meat.capitalize()} it is.")

    spices = ""
    while spices not in spices_list:
        spices = input("What spice? ")
        if spices not in spices_list:
            print(f"Sorry, didn't catch that.")
            waiters_first_suggestion = choice(spices_list)
            waiters_second_suggestion = choice(spices_list)
            while waiters_second_suggestion == waiters_first_suggestion:
                waiters_second_suggestion = choice(spices_list)                
            print(f"How about some {waiters_first_suggestion} or maybe you'd prefer {waiters_second_suggestion}?")
            print(f"I think {waiters_first_suggestion} goes well with {meat}, but it's your call.")
            
    print(f"I will make you some {meat} and {spices} sausage.\n")
    print("I'll be right back with your order.")
    sleep(1)
    print(".")
    sleep(1)
    print(f"Hank! Flop an Adam and Eve on a raft, shingle on a shimmy, burn the British and pour me a cup of mud! Pronto!")
    sleep(3)
    print(".")
    sleep(1)
    print(".")
    sleep(1)
    
    sausage_machine(meat, spices)  

def serve_eggs():
    if eggs > 1:
        print(f"And here's your {eggs} {cook_style} eggs.")
    else:
        print(f"And here's your {eggs} {cook_style} egg.")
    
    print("Enjoy your breakfast.")

def main():

    order_eggs()
    order_sausage()
    serve_eggs()

main()
