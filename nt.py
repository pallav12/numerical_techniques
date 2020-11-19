import sys
import argparse
global a 
global df
def fx(n):
    return eval(a.replace('x',str(n)))

def dfx(n):
    return eval(df.replace('x',str(n))) 

def solve(l,r,n):
    mid=(l+r)/2
    print('lower limit {}, upper limit {}, iteration {}, fx(mid) {}'.format(l,r,n,fx(mid)))
    if(n==0):
        return fx(mid)
    if(fx(mid)<0):
        solve(mid,r,n-1)
    else:
        solve(l,mid,n-1)

def inputEq():
    global a
    print("Enter the equation in one variable (Eg 3*x^2-4*x+5)")
    a=input()
    a=a.replace('^','**')
    a=a.replace(' ','')

def inputDfx():
    global df
    print("Derivative of fx u just entered (Eg 6*x-4)")
    df=input()
    df=df.replace('^','**')
    df=df.replace(' ','')

def newton_bisection():
    inputEq()
    print("Enter lower and upper limits (Spaced real no, Eg 6 11)")
    l,r=map(int,input().split())
    print('Enter number of iteration (Eg 20')
    n=int(input())
    if(fx(l)*fx(r)<0):
        solve(l,r,n)
    else:
        print('Incorrect limits f(l)*f(r) should be <0 ')

def _newton_method(n,guess):
    if(n==0):
        temp=guess-fx(guess)/dfx(guess)
        print('x{}= {} fx{} = {}'.format(n,temp,n,fx(temp)))
        return guess-fx(guess)/dfx(guess)
    nmm=_newton_method(n-1,guess)
    temp=nmm-fx(nmm)/dfx(nmm)
    print('x{}= {} fx{} = {}'.format(n,temp,n,fx(temp)))
    return nmm-fx(nmm)/dfx(nmm)
def newton_method():
    inputEq()
    inputDfx()
    print("Enter number of iteration")
    n=int(input())
    print("Enter known x for which f(x)>0")
    guess=int(input())
    _newton_method(n,guess)

parser = argparse.ArgumentParser("numerical_techniques",formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument("-bis","--bisection_method", help="bisection", action='store_true')
parser.add_argument("-nm", "--newton_method", help="Newton secant method", action='store_true')
args = parser.parse_args()
if(args.bisection_method):
    newton_bisection()
    exit()
if(args.newton_method):
    newton_method()
    exit()
