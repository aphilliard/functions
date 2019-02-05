import sys
sausage_cost = 3.00
account_balance = 20.00

def check_balance(amount):
    if account_balance - amount >= 0:
        return True
    elif account_balance <= 2:
        end_program = input("You don't have enough to buy even one sausage. Quit?")
        if end_program == "yes" or end_program == "y":
            raise SystemExit
    else:
        print("You can't afford it!")
        return False

def buy_sausage():
    global account_balance
    while True:
        try:
            x = int(input("How many sausages?"))
        except (ValueError):
            print("Not a number.")
            continue
        else:
            break
        
    if check_balance(sausage_cost*x):
        account_balance -= sausage_cost*x
        print(f"You bought {x} sausages.")

def main():
    while True:
        print(f"You have {account_balance:.2f} dollars left.")
        buy_sausage()

print(f"You are hungry and you have {account_balance:.2f} dollars in your wallet. Time to buy some tasty sausages!")
print()
main()


    
