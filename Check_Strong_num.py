def fact(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f


num = int(input("Enter the number\n"))

for i in range(0, num + 1):
    sum = 0
    temp = i
    while temp > 0:
        rend = temp % 10
        sum = sum + fact(rend)
        temp = temp // 10

    if sum == i:
        print(f"{i} is strong")
