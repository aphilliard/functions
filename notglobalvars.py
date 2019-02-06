a = 3

def display_a():
    print(f"Print a: {a}")
    
def play_with_a():
    print(f"Print a + 2: {a + 2}")

def use_a():
    print("Now, let's make a new variable based on a's value and call it new_a.")
    new_a = a
    print(f"Variable a's old value is: {new_a}.")
    print(f"Add new_a to new_a: {new_a + new_a}.")
    new_a = a
    print(f"Now let's try to return new_a's value to a: {new_a}")
    
def plug_a_into_me(varval):
    print("We plugged user input into this function.")
    new_a = a
    print(f"Let's add user input's value, which is {varval}, to a: {varval + new_a}.")
 
display_a()
play_with_a()
use_a()
user_input = int(input(f"Type a number to add to a, which equals {a}. "))
plug_a_into_me(user_input)
