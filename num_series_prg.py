def num_series():
    n = int(input("Enter a positive (or negative to end) number: "))
    while n >= 0:
        if n % 2 == 0:
            print(n, "is even.")
        else:
            print(n, "is odd.")
        n = int(input("Enter another number or a negative to quit: "))
num_series()
    
