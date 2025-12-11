from array import *

# # a1=array('i',[1,2,4,6,8])

# # print(a1)
# # print(type(a1))

# # for x in a1:
# #     print(x)

# # for i in range(len(a1)):
# #     print(a1[i],end=" ")


# from array import *

# # a1=array("i",[1,2,3,5,6])
# # print(type(a1),a1)

# # for x in a1:
# #     x*=2
# #     print(x)

# # for z in range(len(a1)):
# #     print(a1[z],end=" ")

# # b=0

# # while b<len(a1):
# #     print(a1[b])
# #     b+=2

# a1=array("i",[12,2,34,5,2])

# print(type(a1),a1)
# # for x in a1:
# #     print(x)
# n=0
# while n<len(a1):
#     print(a1[n])
#     n+=1

# a1.append(23)
# a1.insert(1,3)
# print(a1.pop())
# print(a1)
# a1.reverse()
# print(a1)
# lis=a1.tolist()
# print(lis,type(lis))

# l=[1,2,3,5,5]
# print(l,type(l))

# print(a1.fromlist(l))
# print(a1)
# a1[1]=10
# print(a1)

# Q1
# arr=array("i",[1,4,5,2,3])
# print(sorted(arr))

# # Q2
# lis=[2,3,"taha","anis",4,5]
# new_list=[]
# for item in lis:
#     if(type(item) ==int):
#         new_list.append(item)
# print(new_list)
# Q3
# marks=[34,45,67,56]
# sum=0
# for i in marks:
#     sum+=i
#     print(sum)
# avg=(sum/len(marks))
# print(avg)

# Q4
n=int(input("Enter N: "))
prime=[]
num=2

while len(prime)<n:
    is_prime=True
    for i in range(2,num):
        if(num%i==0):
            is_prime=False
            break
    if(is_prime):
        prime.append(num)
    num+=1
print(prime)

# Q5
# N=int(input("Enter the Number : "))
# a=0
# b=1
# print(a)
# print(b)

# for i in range(1,N+1):
#     c=a+b
#     a=b
#     b=c
#     print(c)
