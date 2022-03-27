x = float(input("請輸入一個X座標:"))
y = float(input("請輸入一個Y座標:"))
if x == 0 and y == 0:
    print("在原點")
else: 
    if x>0 and y>0:
        print("第1象限")
    else: 
        if x<0 and y>0:
            print("第2象限")
        else: 
            if x<0 and y<0:
                print("第3象限")
            else: 
                if x>0 and y<0:
                    print("第四象限")
                else:
                    if x==0 and y>0 or y<0:
                        print("在Y軸上")
                    else:
                        print("在X軸上")