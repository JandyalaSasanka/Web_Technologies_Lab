#J.Sasanka 1602-16-737-042
#My Python Code


def addition(x,y):
    return (x+y)

def subtraction(x,y):
    return (x-y)

def multiply(x,y):
    return (x*y)

def division(x,y):
    return (x/y)

try:
    x=int(input("Enter First Number:\n"))
    y=int(input("Enter Second Number:\n"));
    print ("1.Addition 2.Subtraction 3.Multiplication 4.Division")
    op=input("Enter option\n")

    if(op=='1'):
        print(addition(x,y))
    elif(op=='2'):
        print (subtraction(x,y))
    elif(op=='3'):
        print (multiply(x,y))
    elif(op=='4'):
        print (division(x,y))
    else:
        print ("Enter Correct Option")
except ValueError:
    print("Enter An Integer Value")
    
