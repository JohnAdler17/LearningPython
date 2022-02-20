def sum_squares():
    n = int(input("Enter n: "))
    cnt = 1
    total = 0
    while n >= cnt:
        total += n**2
        n -= 1
    print(total)
sum_squares()
