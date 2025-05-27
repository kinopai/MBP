for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(f"{i}: 3と5の両方の倍数")
    elif i % 3 == 0:
        print(f"{i}: 3の倍数")
    elif i % 5 == 0:
        print(f"{i}: 5の倍数")
