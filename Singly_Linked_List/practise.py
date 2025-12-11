# # class Node:
# #     def __init__(self,item=None,next=None):
# #         self.item=item
# #         self.next=next

# # class SLL:
# #     def __init__(self,start):
# #         self.start=start

# #     def isEmpty(self):
# #         if(self.start==None):
# #             print("this is Empty linkList")


# # n5=Node(1)
# # n4=Node(10,n5)
# # n3=Node(20,n4)                
# # n2=Node(30,n3)
# # n1=Node(40,n2)
# # s1=SLL(n1)



# # # print(s1.start.item)
# # # print(s1.start.next.item)
# # # print(s1.start.next.next.item )
# # # print(n3.item)
# # # print(n3.next)
# # # print(n3.next.item)

# # # current=s1.start
# # # while current.next!=None:
# # #     print(current.item)
# # #     current=current.next


# # n6=Node(60,s1.start)
# # # print(n6.next.item)

# # s1=SLL(n6)

# # current=s1.start
# # while current!=None:
    
# #     print(current.item)
# #     current=current.next



# class Node:
#     def __init__(self,item=None,next=None):
#         self.item=item
#         self.next=next


# class SLL:
#     def __init__(self,start):
#         self.start=start




# n5=Node(50)
# n4=Node(40,n5)
# n3=Node(30,n4)
# n2=Node(20,n3)
# n1=Node(10,n2)


# s=SLL(n1)

# # current=s.start
# # while current.next!=None:
# #     print(current.item)
# #     current=current.next


# n6=Node(33,s.start)
# s=SLL(n6)

# current=s.start
# while current.next!=None:
#     print(current.item)
#     current=current.next





                                                                      ## Insertion at the beginning of the Node


# class Node:
#     def __init__(self,item=None,next=None):
#         self.item=item
#         self.next=next


# class SLL:
#     def __init__(self,start):
#         self.start=start


# n6=Node(70)
# n5=Node(60,n6)
# n4=Node(50,n5)
# n3=Node(40,n4)
# n2=Node(30,n3)
# n1=Node(20,n2)

# s1=SLL(n1)

# # Current=s1.start
# # while Current!=None:
# #     print(Current.item)
# #     Current=Current.next


# n0=Node(10,s1.start)

# s1=SLL(n0)

# current=s1.start
# while current!=None:
#     print(current.item)
#     current=current.next




                                                                                ## Deletion at the Start of the Node

# class Node:
#     def __init__(self,item=None,next=None):
#         self.item=item
#         self.next=next


# class SLL:
#     def __init__(self,start):
#         self.start=start


# n6=Node(70)
# n5=Node(60,n6)
# n4=Node(50,n5)
# n3=Node(40,n4)
# n2=Node(30,n3)
# n1=Node(20,n2)

# s1=SLL(n1)



# current=s1.start.next
# while current!=None:
#     print(current.item)
#     current=current.next





                                                                                ## Deletion at the End of the Node

# class Node:
#     def __init__(self,item=None,next=None):
#         self.item=item
#         self.next=next


# class SLL:
#     def __init__(self,start):
#         self.start=start


# n7=Node(80)
# n6=Node(70,n7)
# n5=Node(60,n6)
# n4=Node(50,n5)
# n3=Node(40,n4)
# n2=Node(30,n3)
# n1=Node(20,n2)

# s1=SLL(n1)



# current=s1.start
# while current.next!=None:
#     if current.next.next==None:
#         print(current.item)
#         current.next=None
#         break   
#     print(current.item)
#     current=current.next



                                                                        # Delete at the Particular Level

# class Node:
#     def __init__(self,item=None,next=None):
#         self.item=item
#         self.next=next


# class SLL:
#     def __init__(self,start=None):
#         self.start=start


# n7=Node(70)
# n6=Node(60,n7)
# n5=Node(50,n6)
# n4=Node(40,n5)
# n3=Node(30,n4)
# n2=Node(20,n3)
# n1=Node(10,n2)
# n0=Node(0,n1)

# s1=SLL(n0)


# current=s1.start

# while current != None:
#     if current.item==30:
#         current=current.next
#         continue
#     print(current.item)
#     current=current.next
    





                                                                    #  Insertion at the end of Linked list


# class Node:
#     def __init__(self,item=None,next=None):
#         self.item=item
#         self.next=next


# class SLL:
#     def __init__(self,start=None):
#         self.start=start


# n7=Node(70)
# n6=Node(60,n7)
# n5=Node(50,n6)
# n4=Node(40,n5)
# n3=Node(30,n4)
# n2=Node(20,n3)
# n1=Node(10,n2)
# n0=Node(0,n1)

# s1=SLL(n0)


# current=s1.start
# n8=Node(80)



# while current.next is not None:   # move until last node
#     print(current.item)
#     current = current.next

# current.next = n8
# print(current.item)
# print(n8.item)







                                                                        # Insertion a node at the specific position
# class Node:
#     def __init__(self,item=None,next=None):
#         self.item=item
#         self.next=next


# class SLL(Node):
#     def __init__(self,start=None):
#         self.start=start
        

#     def checkEmpty(self):
#         if self.start ==None:
#             print("SLL is Empty ")
#             return self.start==None
        

#     def insert_at_start(self,item):
#         if not self.checkEmpty():
#                 n=Node(item,self.start)
#                 self.start=n
#                 print("Node is Added to SLL")
#         else:
#             n=Node(item)
    

#     def insert_at_last(self,item):
#         n=Node(item)
#         if not self.checkEmpty():
#             current=self.start

#             while current.next is not None:
#                 current=current.next
#             current.next=n
#         else:
#             self.start=n



#     def search(self,item):
#         head=self.start
#         count=0
#         while head is not None:
#             if head.item==item:
#                 print(f"{item} is Found at Node {count}")
#             head=head.next
#             count+=1





# n3=Node(30)
# n2=Node(20,n3)
# n1=Node(10,n2)


# s1=SLL(n1)

# s1.insert_at_start(12)
# s1.insert_at_start(15)
# s1.insert_at_last(12)
# s1.search(20)

# Current=s1.start


# while Current is not None:
#     print(Current.item)
#     Current=Current.next




# class Node:
#     def __init__(self,item=None,next=None):
#         self.item=item
#         self.next=next

# class SLL:
#     def __init__(self,start=None):
#         self.start=start

    
#     def is_Empty(self):
#         if self.start==None:
#             print("Empty")
#             return self.start==None
        
#     def insert_at_start(self,x):
#         if not self.is_Empty():
#             n=Node(x,self.start)
#             self.start=n
#             print("Node is Added to SLL")
#         else:
#             n=Node(x)
#             self.start=n

#     def insert_at_last(self,x):
#         if not self.is_Empty():
#             n=Node(x)
#             current=self.start
#             while current.next is not None:
#                 current=current.next
#             current.next=n
#         else:
#             n=Node(x)
#             self.start=n

#     def search(self,x):
#         if self.is_Empty():
#             print("This LinkList is Empty")
#         else:
#             current=self.start
#             index=-1
            
#             while current is not None:
#                 if current.item==x:
#                     print(f"{x} is Found at Node {index}")
#                 index+=1
#                 current=current.next

 
# n5=Node(50)
# n4=Node(40,n5)
# n3=Node(30,n4)
# n2=Node(20,n3)
# n1=Node(10,n2)
# n0=Node(00,n1)


# s1=SLL(n0)


# Current=s1.start

# while Current is not None:
#     print(Current.item)
#     Current=Current.next

# s1.is_Empty()

# s1.insert_at_start(-10)

# Current=s1.start

# while Current is not None:
#     print(Current.item)
#     Current=Current.next


# s1.insert_at_last(60)


# Current=s1.start

# while Current is not None:
#     print(Current.item)
#     Current=Current.next


# s1.search(30)





# class Node:
#     def __init__(self,item=None,next=None):
#         self.item=item
#         self.next=next


# class SLL:
#     def __init__(self,start=None):
#         self.start=start

#     def is_Empty(self):
#         if  self.start ==None:
#             print("LinkList is Empty")
#             return self.start== None
        

#     def insert_at_start(self,x):
#         if not self.is_Empty():
#             n=Node(x,self.start)
#             self.start=n
#             print("Node is Added to SLL")
#         else:
#             n=Node(x)
#             self.start=n
#             print("Insert at Start\n")
    

#     def insert_at_last(self,x):
#         if not self.is_Empty():
#             n=Node(x)
#             current=self.start
#             while current.next is not None:
#                 current=current.next
#             current.next=n
#         else:
#             n=Node(x)
#             self.start=n


#     def search(self,x):
#         current=self.start
#         if self.is_Empty():
#             pass
#         else:
#             while current is not None:
#                 if current.item==x:
#                     print(f"\nFound {x}")
#                     return current
#                 current=current.next



#     def insert_After(self,N,x):
#         if self.start==N:
#             n=Node(x,self.start.next.next)
#             self.start.next=n
#         else:
#             current=self.start
#             while current is not None:
#                 if current==N:
#                     n=Node(x,current.next)
#                     current.next=n
#                 current=current.next


#     def print_List(self):
#         current=self.start
#         while current is not None:
#             print(current.item,end=" ")
            
#             current=current.next
#         print("\n")


#     def delete_first(self):
#         if self.start is not None:
#             self.start=self.start.next


#     def delete_last(self):
#         if self.start is None:
#             pass
#         elif self.start.next is None:
#             self.start=None
#         else:
#             current=self.start
#             while current is not None:
#                 if current.next.next==None:
#                     current.next=None
#                 current=current.next


#     def delete_item(self,x):
#         if self.start==None:
#             pass
#         elif self.start.next is None:
#             if self.start.item==x:
#                 self.start=None
#         else:
#             current=self.start
#             if current.item==x:
#                 self.start=current.next
#             while current is not None:
#                 if current.next.item==x:
#                     current.next=current.next.next
#                     break
#                 current=current.next


#     def __iter__(self):
#         return iterator(self.start)


# class iterator:
#     def __init__(self,start):
#         self.current=start

#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if not self.current:
#             raise StopIteration
#         else:
#             data=self.current.item
#             self.current=self.current.next
#             return data



# s1=SLL()


# s1.insert_at_start(10)
# s1.insert_at_last(20)
# s1.insert_at_last(30)
# s1.insert_at_last(40)
# s1.insert_at_last(50)

# # current=s1.start

# # while current is not None:
# #     print(current.item)
# #     current=current.next

# s1.print_List()


# s1.search(20)

# s1.insert_After(s1.search(30),35)
# s1.print_List()

# s1.delete_item(35)
# s1.print_List()



# for i in s1:
#     print(i)




class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next


class SLL:
    def __init__(self,start=None):
        self.start=start

    def is_Empty(self):
        if self.start==None:
            return self.start==None



    def insert_at_start(self,x):
        if self.is_Empty():
            n=Node(x)
            self.start=n
        else:
            n=Node(x,self.start)
            self.start=n

    def insert_at_last(self,x):
        if self.is_Empty():
            n=Node(x)
            self.start=n
        else:
            n=Node(x)
            current=self.start
            while current.next is not None:
                current=current.next
            current.next=n
    

    def search(self,x):
        current=self.start
        while current is not None:
            if current.item==x:
                print(f"\nFound {current.item}")
                return current
            current=current.next
    

    def insert_after(self,N,x):
        if self.start==N:
            n=Node(x,self.start.next)
            self.start.next=n
        else:
            current=self.start
            while current is not None:
                if current==N:
                    n=Node(x,current.next)
                    current.next=n
                current=current.next


    def print_list(self):
        current=self.start
        while current is not None:
            print(current.item,end=" ")
            current=current.next

    
    def delete_first(self):
        if self.start !=None:
            self.start=self.start.next
            print("\n Deleting First Element")
    
    def delete_Last(self):
        if self.start==None:
            pass
        elif self.start.next==None:
            self.start=None
        else:
            current=self.start
            while current is not None:
                if current.next.next==None:
                    current.next=None
                current=current.next
            print("\n Deleting Last Element")


    def delete_item(self,x):
        if self.start==None:
            pass
        elif self.start.next==None:
            if self.start.item==x:
                self.start=None
        else:
            current=self.start
            if current.item==x:
                self.start=current.next
            while current is not None:
                if current.next.item==x:
                    current.next=current.next.next
                    break
                current=current.next
        print("\n Deleting Selected Element")

    def __iter__(self):
        return iterator(self.start)


class iterator:
    def __init__(self,start):
        self.current=start

    def __iter__(self):
        return self
    

    def __next__(self):
        if not self.current:
            raise StopIteration
        
        data=self.current.item
        self.current=self.current.next
        return data

 
s1=SLL()
s1.insert_at_start(10)
s1.insert_at_start(0)
s1.insert_at_start(-10)
s1.insert_at_last(20)
s1.insert_at_last(30)
# s1.print_list()

# s1.search(20)

s1.insert_after(s1.search(20),25)
s1.print_list()

s1.delete_first()
s1.print_list()


s1.delete_Last()
s1.print_list()

s1.delete_item(20)
s1.print_list()


for i in s1:
    print(i)



