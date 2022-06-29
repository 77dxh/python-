a=int(input('搭了幾次電梯?'))
n=1
sum=0
for i in range(0,a):
    t=int(input(i+1))
    if t-n>0:
        sum=(t-n)*20+sum
        n=t
    elif t-n<0:
        sum=sum+(n-t)*10
        n=t
print(sum,'元')