# this function adds two numbers
def add(x,y):
    print(x+y)

# this function subtracts two numbers
def sub(x,y):
    print(x-y)

# this function multiplies two numbers
def multi(x,y):
    print(x*y)

# this function divides two numbers
def div(x,y):
    print(x/y)
#################################################
#Start of program

print("welcome to the calc")
while(True):
    print(" what would u like to do")
    print("select: (a)dd (s)ubtract (m)ultiply (d)ivide (q)uit")

    user_choice=input(": ")
    if user_choice =='a':
        x=int(input("Enter your first number: "))
        y=int(input("Enter your second number: "))
        add(x,y)

    elif user_choice == 's':
        x=int(input("Enter your first number: "))
        y=int(input("Enter your second number: "))
        sub(x,y)

    elif user_choice == 'm':
        x=int(input("Enter your first number: "))
        y=int(input("Enter your second number: "))
        multi(x,y)

    elif user_choice == 'd':
        x=int(input("Enter your first number: "))
        y=int(input("Enter your second number: "))
        div(x,y)

    elif user_choice == 'q':
        print("Closing Program...")
        break

    else:
        print("That isn't one of the options silly!")
