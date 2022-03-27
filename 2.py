used = float(input())

if used <= 120:
    summer = used * 2.10
    non_summer = used * 2.10
elif 120 < used <= 330:
    summer = (120*2.10) + (used - 120) * 3.02
    non_summer = (120*2.10) + (used - 120) * 2.68
elif 330 < used <= 500:
    summer = (120*2.10) + (210 * 3.02) + (used - 330) * 4.39
    non_summer = (120*2.10) + (210 * 2.68) + (used - 330) * 3.61
elif 500 < used <= 700:
    summer = (120*2.10) + (210 * 3.02) + (170 * 4.39) + (used - 500) * 4.97
    non_summer = (120*2.10) + (210 * 2.68) + (170 * 3.61) + (used - 500) * 4.01
elif 700 < used:
    summer = (120*2.10) + (210 * 3.02) + (170 * 4.39) + (200 * 4.97) + (used - 700) * 5.63
    non_summer = (120*2.10) + (210 * 2.68) + (170 * 3.61) + (200 * 4.01) + (used - 700) * 4.50

print(f"Summer months:{summer:.2f}")
print(f"Non-Summer months:{non_summer:.2f}")