def factorial(n):
    if n==1:
        return 1
    else:
        return(n*factorial(n-1))
x=int(input("enter the num"))
res=factorial(x)
print("the factorial is",res)
