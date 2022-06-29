a=int(input('a'))
b=int(input('b'))
c=int(input('c'))
x1=((-b)+(b**2-4*a*c)**0.5)/2/a
x2=((-b)-(b**2-4*a*c)**0.5)/2/a
if b**2-4*a*c>=0:
    if x1==x2:
        print('%.0f'%(x1))
    else:
        print('%.0f'%(x1))
        print('%.0f'%(x2))
else:
    print('0')