print('Welcome to the Tower of Hanoi Problem Solver.')
n=int(input('Please enter the number of discs on the a-pillar:'))
def x(n,a,b,c):
    if n>0:
        x(n-1,a,c,b)
        print('Move the top disc of the %s bar to the top of the %s bar'%(a,c))
        x(n-1,b,a,c)
x(n,'A','B','C')

