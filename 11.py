month =int(input("請輸入月："))
day = int(input("請輸入日期："))
name = ('摩羯座','水瓶座','雙魚座','白羊座','金牛座','雙子座','巨蟹座','獅子座','處女座','天秤座','天蠍座','射手座')
days =((1, 21),(2, 19),(3, 21),(4, 21),(5, 21),(6, 22),(7, 23),(8, 23),(9, 23),(10, 23),(11, 22),(12, 21))

for num in range(len(days)):
    if days[num] >= (month, day):
        print("星座為 %s"%(name[num]))
        break
    elif month == 12 and (day > 21 and day <= 31):
        print("星座為 %s"%(name[0]))
        break
    elif month >12 or day > 31:
        print("請重新輸入")
        break