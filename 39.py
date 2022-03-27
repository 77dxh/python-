for i in range (1,6):
    for a in range(5-i):
        print(' ',end='')
    for a in range(2*i+1):
        if a%2==0:
            print(' ',end='')
        else:
            print('*',end='')
    print()
for i in range (5,1,-1):
    for a in range(5-i):
        print(' ',end='')
    for a in range(2*i-1):
        if a%2==0:
            print(' ',end='')
        else:
            print('*',end='')
    print()
