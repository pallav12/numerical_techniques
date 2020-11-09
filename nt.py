import sys
import argparse

global a 

def fx(n):
    return eval(a.replace('x',str(n)))
def solve(l,r,n):
    mid=(l+r)/2
    print('lower limit {}, upper limit {}, iteration {}, fx(mid) {}'.format(l,r,n,fx(mid)))
    if(n==0):
        return fx(mid)
    if(fx(mid)<0):
        solve(mid,r,n-1)
    else:
        solve(l,mid,n-1)

def newton_bisection():
    global a
    print("Enter the equation in one variable (Eg 3*x^2-4*x+5)")
    a=input()
    print("Enter lower and upper limits (Spaced real no, Eg 6 11)")
    l,r=map(int,input().split())
    print('Enter number of iteration (Eg 20')
    n=int(input())
    a=a.replace('^','**')
    if(fx(l)*fx(r)<0):
        solve(l,r,n)
    else:
        print('Incorrect limits f(l)*f(r) should be <0 ')
parser = argparse.ArgumentParser("numerical_techniques",formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument("-nb","--newton_bisection", help="Newton bisection", action='store_true')
args = parser.parse_args()
if(args.newton_bisection):
    newton_bisection()
    exit()
