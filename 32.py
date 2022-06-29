m=int(input('小明身上有幾元:0<=m<=100'))
n=int(input('販賣機有幾種飲料(1<=n<=30):'))
price=[]
sum=0
if m>100 or m<0:
    print('輸入錯誤')
elif n>30 or n<1:
    print('輸入錯誤')
for i in range(0,n):
    a=int(input('第'+str(i+1)+'種價錢$'))
    if a <10 or a>50:
        print('輸入錯誤')
    price.append(a)
for s in range(0,n):
    if m>=price[s]:
        sum+=1
print('總共可以買'+str(sum)+'種飲料')