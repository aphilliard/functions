def invert(x):
    try:
        i = 1.0 / x
    except:
        print("You can't do that!")
    else:
        print("Reciprocal of", x, "is", i)

div_num = int(input("Type a number"))
invert(div_num)