from math import *

prime = list()
num = input("請輸入正整數:")
length = len(num)
max_prime = 0
def is_prime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return 0
    return 1

for check in range(2, int(num)):
    if is_prime(check):
        prime.append(check)

for l in range(length):
    for r in range(l + 1, length + 1):
        item = int(num[l:r])

        if (item in prime) and (item > max_prime):
            max_prime = item

if max_prime == 0:
    print("No prime found")
else:
    print(f"子字串中最大質數值為:{max_prime}")