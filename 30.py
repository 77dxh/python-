right = ['1','2',"3","4"]

while True:
    a=0
    b=0
    user =list(input('猜四位數字:'))
    if user.count('0')==4:
        print('結束')
        break
    if len(user)==4:
        for i in range(4):
            if (right[i]==user[i]):
                a+=1
            elif(right.count(user[i])==1 and right[i]!=user[i]):
                b+=1
        print(str(a)+'A',str(b)+"B")
    elif len(user)!=4:
        print('輸入錯誤')
    if a==4:
        break