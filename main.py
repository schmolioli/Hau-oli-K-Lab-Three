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
print("what would u like to do")
print("select: (a)dd (s)ubtract (m)ultiply (d)ivide (q)uit")


x=int(input("Enter your first number: "))
y=int(input("Enter your second number: "))

add(x,y)
sub(x,y)
multi(x,y)
div(x,y)