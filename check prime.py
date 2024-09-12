Num = int(input("enter a number:"))
count = 0
for i in range(2, (Num//2 + 1)):
    if(Num % i == 0):
        count = count + 1
        break
    if(count == 0 and Num != 1):
        print("%d is a prime number"%Num)
    else:
        print("%dis not a prime number"%Num)
