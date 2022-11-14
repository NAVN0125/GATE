
def fact(x):
    sum = 1
    for x in range(1,x+1):
        sum = sum*x
        x=x+1
    print(sum)
x = int(input("Enter a number: "))
fact(x)