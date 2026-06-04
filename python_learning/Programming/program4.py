#Fibonacci
# n=10
# a,b=0,1
# for i in range(n):
#     print(a, end=" ")
#     a,b=b,a+b

#Method-2 Using def
def fib(n):
    if n<=1:
        return n
    return fib(n-1)+fib(n-2)

for i in range(15):
    print(fib(i), end=" ")