L = list()
L_max = list()
L_min = list()

for i in range(10):
    a = int(input(f"請輸入第{i}個數字:"))
    L.append(a)

for maximum in range(3):
    b = max(L)
    L_max.append(b)
    L.remove(b)

for minimum in range(3):
    c = min(L)
    L_min.append(c)
    L.remove(c)

L_min.reverse()

print(f"最大的3個數字為:{L_max[0]},{L_max[1]},{L_max[2]}")
print(f"最小的3個數字為:{L_min[0]},{L_min[1]},{L_min[2]}")
    