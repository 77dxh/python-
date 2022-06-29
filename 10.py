n = input('請輸入轉置矩陣').split(' ')
math=[]
g=[]
for i in range(1,int(n[0])+1):
    a=input('輸入矩陣數值第'+str(i)+'列為').split(' ')
    math.append(a)
for i in range(0,int(n[0])):
    for j in range(0,int(n[1])):
        g.append(math[i][j])
for s in range(0,int(n[1])):
    print('輸出矩陣數值第'+str(s+1)+'列為',g[s],g[s+int(n[1])])