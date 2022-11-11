
logo = """
 _____________________
|  _________________  |
| | AARAV       0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""



print(logo)

 # YO LOL

# add
def add(n1,n2):
    return n1 + n2

# substract
def sub(n1,n2):
    return n1 - n2

# multiplie
def multi(n1,n2):
    return n1 * n2

# divivde
def div(n1,n2):
    return n1 / n2


calc = {
    "+" : add,
    "-" : sub,
    "*" : multi,
    "/" : div
}
def calculator():
    n1 = float(input("what is your first num: " ))
    
    for symbol in calc:
        print(symbol)
    op = input("Enter a symbol from above: ")
    n2 = float(input("what is your second num: "))
    
    answer = calc[op](n1,n2)
    
    print(f"{n1} {op} {n2} = {answer}")
    
    while True:
        
        direct = input(f"do you want to carry on the calculation with {answer}(yes or no) if you want to make a new calculation type new: ").lower()
        if direct == "no":
            break
        elif direct == "yes":
            num = float(input("enter your number: "))
            op = input("Enter a symbol: ")
            
            previus_answer = answer
            answer = calc[op](answer,num)
            print(f"{previus_answer} {op} {num} = {answer}")
        elif direct == "new":
            calculator()
            break
            
calculator()
    

