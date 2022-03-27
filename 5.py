t=n=1
m=int(input("請輸入一個正整數"))
while(t<=m):
    t*=n
    n+=1
print(n-1,"階層為",t,"大於",n)