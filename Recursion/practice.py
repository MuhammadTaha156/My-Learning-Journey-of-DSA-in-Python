# print("N Numbers")
# def N(n):
#     if n>0:
#         N(n-1)
#         print(n,end=" ")
# N(10)

# print()

# print("\nN Reverse Numbers")
# # Reverse
# def N_Reverse(n):
#     if n>0:
#         print(n,end=" ")
#         N_Reverse(n-1)
# N_Reverse(10)


# print()
# print("\nODD Numbers")
# # ODD N numbers
# def odd(n):
#     if n>0:
#         odd(n-1)
#         if n%2!=0:
#             print(n,end=" ")

# odd(10)

# print()

# print("\nEVEN Numbers")
# # EVEN N numbers
# def Even(n):
#     if n>0:
#         Even(n-1)
#         if n%2==0:
#             print(n,end=" ")

# Even(10)

# print()
# print("\nODD Reverse Numbers")
# # Odd N number in Reverse

# def odd_R(n):
#     if n==0:
#         return 0
#     if n%2!=0:
#         print(n,end=" ")
#     odd_R(n-1)
        
# odd_R(10)
 
# print("\nEVEN Reverse Numbers")
# def Even_R(n):
#     if n>0:
#         print(2*n,end=" ")
#         Even_R(n-1)
# Even_R(10)
 
# print("\odd Reverse Numbers")
# def Odd_R(n):
#     if n>0:
#         print(2*n-1,end=" ")
#         Even_R(n-1)
# Odd_R(10)



# def sum(n):
#     if n==1:
#         return 1
#     s=n+sum(n-1)
#     return s

# print(sum(10))

# def odd(n):
#     if n==0:
#         return 0
    
#     s=2*n-1+odd(n-1)
    
#     return s
    
# print(odd(10))


# def even(n):
#     if n==0:
#         return 0
#     s=2*n+even(n-1)
#     return s

# print(even(10))



# def fact(n):
#     if n==1:
#         return 1
#     fac=n*fact(n-1)
#     return fac

# print(fact(10))

# def square(n):
#     if n==0 or n==1:
#         return 1
    
#     s=n**2+square(n-1)
#     return s

# print(square(10))

