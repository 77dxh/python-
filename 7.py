
a = int(input('通話費率($186,$386,$586,$986):'))
b = int(input('通話時間:'))
if (a == 186) :
    if int(b*0.09<=186*2):
        b1 = b*0.9*0.09
        print('通話費為:%d'%(b1))
    else:
        b1 = b*0.8*0.09
        print('通話費為:%d'%(b1))
elif (a == 386) :
    if int(b*0.08<=386*2):
        b1 = b*0.8*0.08
        print('通話費為:%d'%(b1))
    else:
        b1 = b*0.7*0.08
        print('通話費為:%d'%(b1))
elif (a == 586) :
    if int(b*0.07<=186*2):
        b1 = b*0.7*0.07
        print('通話費為:%d'%(b1))
    else:
        b1 = b*0.6*0.07
        print('通話費為:%d'%(b1))
elif (a == 986) :
    if int(b*0.06<=186*2):
        b1 = b*0.6*0.06
        print('通話費為:%d'%(b1))
    else:
        b1 = b*0.5*0.06
        print('通話費為:%d'%(b1))
else:
    print('輸入錯誤')