
def newton_bisection():
    print("Enter the equation in one variable")
    a=input()
    print("Enter lower and upper limits")
    l,r=map(int,input().split())
    print('Enter number of iteration')
    n=input()
    a=a.replace('^','**')
    a=a.replace('x','2')
    print(eval(a))
