# def func(n):
#     if n>0:
#         func(n-1)
#         print(n,end=" ")

# func(10)


# def func(n):
#     if n>0:
#         print(n,end=" ")
#         func(n-1)

# func(10)

# def func(n):
#     if n>0:
#         func(n-1)
#         if n%2!=0:
#             print(n,end=" ")
# func(10)


# def func(n):
#     if n>0:
#         func(n-1)
#         print(n*2,end=" ")
# func(10)


# def fucn(n):
#     if n>0:
#         print(2*n-1,end=" ")
#         fucn(n-1)
# fucn(10)

# def func(n):
#     if n>0:
#         print(2*n,end=" ")
#         func(n-1)

# func(10)

# def sum(n):
#     if n==0:
#         return 0
#     return n+sum(n-1)

# print(sum(10))

# def odds(n):
#     if n==1:
#         return 1
#     return 2*n-1+odds(n-1)

# print(odds(10))

# def Evens(n):
#     if n==0:
#         return 0
#     return 2*n+Evens(n-1)

# print(Evens(10))


# def factorial(n):
#     if n==1:
#         return 1
#     return n*factorial(n-1)
# print(factorial(20))
    

# def square(n):
#     if n==1:
#         return 1
#     return n**2+square(n-1)
# print(square(5))




def func(n):
    if n==1:
        return 1
    s=n**2+func(n-1)
    return s

print(func(10))









