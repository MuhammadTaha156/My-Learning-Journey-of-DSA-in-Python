# class Node:
#     def __init__(self,prev=None,item=None,next=None):
#         self.prev=prev
#         self.item=item
#         self.next=next

# class DLL: 
#     def __init__(self,start=None):
#         self.start=start

#     def is_Empty(self):
#         return self.start ==None

#     def insert_At_start(self,x):
#            n=Node(None,x,self.start)
#            if not self.is_Empty():
#                 self.start.prev=n
#            self.start=n
           
#     def insert_At_last(self,x):
#         if self.is_Empty():
#              n=Node(None,x)
#              self.start=n
#         else:
#             current=self.start
#             while current.next is not None:
#                 current=current.next
#             n=Node(current,x,None)
#             current.next=n            


#     def search(self,x):
#         current=self.start
#         while current is not None:
#             if current.item==x:
#                 print(f"{current.item} Found")
#                 return current
#             current=current.next
#         return None


#     # def insert_After(self,N,x):
#     #     if  self.start==N:
#     #         n=Node(self.start,x,self.start.next)
#     #         self.start.next.prev=n
#     #         self.start.next=n
#     #     else:
#     #         current=self.start
#     #         while current is not None:
#     #             if current==N:
#     #                 n=Node(current,x,current.next)
#     #                 current.next.prev=N
#     #                 current.next=N
#     #             current=current.next
                

#     def insert_After(self,N,x):
#         if  N is not None:
#             n=Node(N,x,N.next)
#             if N.next is not None:
#                 N.next.prev=N
#             N.next=n
                


#     def print_List(self):
#         current=self.start
#         while current is not None:
#             print(current.item,end=" ")
#             current=current.next

#     # def delete_first(self):
#     #     if self.start.next==None:
#     #         self.start=None
#     #     elif not self.is_Empty():
#     #         self.start.next.prev=None
#     #         self.start=self.start.next


#     def delete_first(self):
#         if self.start !=None:
#             self.start=self.start.next
#             if self.start is not None:
#                 self.start.prev=None


#     def delete_Last(self):
        
#         if self.is_Empty():
#             print("LinkList is Empty")
#         elif self.start.next==None:
#             self.start=None
#         else:
#             current=self.start
#             while current.next is not None:
#                 current=current.next
#             current.prev.next=None
#             current.prev=None


#     # def delete_item(self,x):
#     #     if self.is_Empty():
#     #         print("Linked List is Empty")
#     #         return
#     #     elif(self.start.next==None):
#     #         if self.start.item==x:
#     #             self.start=None
#     #         else:
#     #             print("Item not Found")
#     #     else:
#     #          current=self.start
#     #          if current.item==x:
#     #              self.start=current.next
#     #              current.next.prev=None
#     #          else:
#     #             while current is not None:
#     #                 if current.item==x:
#     #                     if current.next is not None:
#     #                         current.next.prev=current.prev
#     #                     current.prev.next=current.next
#     #                     current.next=None
#     #                     current.prev=None
#     #                     break
                    
#     #                 current=current.next

            
#     def delete_item(self, x):
#         if self.is_Empty():
#             print("Linked List is Empty")
#             return

#         current = self.start
#         while current is not None:
#             if current.item == x:
#                 if current.next:
#                     current.next.prev = current.prev
#                 if current.prev:
#                     current.prev.next = current.next
#                 else:
#                     self.start = current.next
#                 print(f"Deleted item: {x}")
#                 return
#             current = current.next

#         print("Item not found")

#     def __iter__(self):
#         return DLL_iterator(self.start)



# class DLL_iterator:
#     def __init__(self,start=None):
#         self.current=start

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.current==None:
#             raise StopIteration
        
#         data=self.current.item
#         self.current=self.current.next
#         return data

    

# D=DLL()
# D.insert_At_start(10)
# D.insert_At_start(0)
# D.insert_At_last(20)
# D.insert_At_last(30)
# D.insert_At_last(40)
# D.insert_At_last(50)
# D.insert_After(D.search(20),25)
# D.print_List()
# # for i in D:
# #     print(i,end="_")

# D.delete_first()
# print("\n")
# D.print_List()

# D.delete_Last()
# print("\n")
# D.print_List()

# D.delete_item(30)
# print("\n")
# D.print_List()







class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next

class DLL:
    def __init__(self,start=None):
        self.start=start

    def is_Empty(self):
        return self.start==None

    def insert_at_start(self,x):
        if self.is_Empty():
            n=Node(None,x)
        if not self.is_Empty():
            current=self.start
            n=Node(None,x,current)
            current.prev=n
        self.start=n

    def insert_at_last(self,x):
        if self.is_Empty():
            n=Node(None,x)
            self.start=n
        if not self.is_Empty():
            current=self.start
            while current.next is not None:
                current=current.next
            n=Node(current,x,None)
            current.next=n
        

    def search(self,x):
        current=self.start
        while current is not None:
            if current.item==x:
                print(f"{current.item } Found")
                return current
            current=current.next

    def print_list(self):
        current=self.start
        while current is not None:
            print(current.item,end=" ")
            current=current.next

    def insert_after(self,N,x):
        current=self.start
        while current is not None:
            if current==N:
                n=Node(current,x,current.next)
                current.next.prev=n
                current.next=n
            current=current.next

    def delete_first(self):
        if self.is_Empty():
            print("Linklist is Empty")
        if self.start.next:
            self.start.next.prev=None
            self.start=self.start.next
        else:
            self.start=None

    def delete_last(self):
        if self.is_Empty():
            print("Linklist is Empty")
        elif self.start.next==None:
            self.start=None
        else:
            while current.next.next is not None:
                current=current.next
            current.next.prev=None
            current.next=None
    
            self.start=None

    def delete_item(self,x):
        if self.is_Empty():
            print("Linklist is Empty")
        else:
            current=self.start
            while current is not None:
                if current.item==x:
                    if current.next:
                        current.next.prev=current.prev
                    if current.prev:
                        current.prev.next=current.next
                    else:
                        self.start=current.next
                    print(f"Deleted item: {x}")
                    return                                  
                current=current.next
            print("Item not found")


    def __iter__(self):
        return iterator(self.start)

class iterator:
    def __init__(self,start=None):
        self.current=start

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current==None:
            raise StopIteration
        data=self.current.item
        self.current=self.current.next
        return data

d=DLL()
d.insert_at_start(20)        
d.insert_at_start(10)        
d.insert_at_start(0)        
# d.print_list()

d.insert_at_last(30)
d.insert_at_last(40)

d.insert_after(d.search(30),35)
d.print_list()
print("\n")
d.delete_first()
d.print_list()
print("\n")
d.delete_item(45)
d.print_list()

print("\n")

for i in d:
    print(i)








