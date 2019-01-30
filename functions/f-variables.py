def f():
    print("variable a is:", a)
    print("variable b is:", b)
    c = (a+b)
    print("Let's create a variable called 'c' and make it the sum of a and b.")
    print("You can print c inside the function:")
    print("variable c is:", c)

def d():
    print("Now we're running another function and trying to print c inside it. That won't work!")
    try:
        print(c)
    except:
        print("That was dumb!")
    

a = 1
b = 2
# c = 3
e = 10

f()
d()

print("Let's try and print the value of c outside of those functions:")
try:
    print(c)
except:
    print("That didn't work!")