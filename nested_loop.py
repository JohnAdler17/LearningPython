def main():
    i = 1
    cnt = 0
    while i < 10000:
       prime = True
       for j in range(2, i):
           if i % j == 0:
               prime = False
               break
       if prime:
           print(i, end=' ')
           cnt += 1
           if cnt > 50:
               break
       i = i + 1

main()
