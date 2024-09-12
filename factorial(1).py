n=int(input("enter a number"))
factorial=1
if int(n)>=1:
    for i in range(1,int(n)+1):
     factorial=factorial*i
    print("factorial of ",n,"is:",factorial)
