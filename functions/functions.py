def to_celsius(t):
    return (t - 32.0) * 5.0 / 9.0

temp = int(input("Temp in farenheit?\n"))

if int(to_celsius(temp)) > 30:
    print("Damn! It's hot!")
elif int(to_celsius(temp)) < 1:
    print("Brrrr!")

print(f"It's {int(to_celsius(temp))} outside!")