a = int(input('第一行正整數為:'))
b = input('第二行數列中的數字為:')
b1 = b.split(' ')
if len(b1)==a :
    b2 = set(b1)
    if len(b2)==len(b1):
        print('每個值剛好只出現一次')
    else:
        print('最大出現次數的數字為:',max(b1,key=b1.count))
        print('出現次數為:',b1.count(max(b1,key=b1.count)))
else:
    print('輸入錯誤')