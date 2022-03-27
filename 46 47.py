style = input("處理方式(1)字典(2)串列:")

if style == '1':
    medal = dict()

    for i in range(4):
        record = input()
        record = record.split()

        medal[record[0]] = record[1]

    print(f"金牌得到{medal['金']}面")
    print(f"銀牌得到{medal['銀']}面")
    print(f"銅牌得到{medal['銅']}面")
    print(f"優牌得到{medal['優']}面")
elif style == '2':
    medal = list()

    for i in range(4):
        record = input()
        record = record.split()

        medal.append(record)

    for item in medal:
        print(f"{item[0]}牌得到{item[1]}面")
