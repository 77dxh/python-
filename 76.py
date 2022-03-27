code = input("請輸入傳送密碼(6位數):")

while len(code) < 6:
    code = input("請輸入傳送密碼(6位數):")

encrypted = str()
match = {'4': 1, '1': 2, '5': 3, '2': 4, '6': 5, '3': 6, '0': 0}

for i in code:
    ans = match.get(i)
    encrypted += str(ans)

print(f"解密後的密碼:{encrypted}")

