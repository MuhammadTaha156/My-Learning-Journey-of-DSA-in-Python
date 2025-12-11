

class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next


class CLL:
    def __init__(self,last=None):
        self.last=last


    def is_Empty(self):
        return self.last==None

    def insert_at_start(self,x):
        n=Node(x)
        if self.is_Empty():
            n.next=n
            self.last=n
        else:
            n.next=self.last.next
            self.last.next=n

    def insert_at_last(self,x):
        n=Node(x)
        if self.is_Empty():
            n.next=n
            self.last=n
        else:
            n.next=self.last.next
            self.last.next=n
            self.last=n

    def search(self,x):
        if self.is_Empty():
            print("Circular Linked List is Empty\n")
            return None
        current = self.last.next
        while current is not self.last:
            if current.item==x:
                print(f"{current.item} Found\n")
                return current
            current=current.next
        if current.item==x:
            print(f"{current.item} Found\n")
            return current
        return None

    def insert_After(self,N,x):
        if self.is_Empty():
            print("Linked List is Empty")
            pass
        if N is not None:
            n=Node(x,N.next)
            N.next=n
            if N==self.last:
                self.last=n


    def print_list(self):
        if not self.is_Empty():
            current=self.last.next
            while current is not self.last:
                print(current.item,end=" ")
                current=current.next
            print(current.item)
        else:
            print("Link List is Empty")


    def delete_first(self):
        if  self.is_Empty():
            print("Circular Link List is Empty")
        elif self.last.next==self.last:
            self.last=None
        else:
            self.last.next=self.last.next.next
            

    def delete_last(self):
        if self.is_Empty():
            print("Circular Link List is Empty")
        elif(self.last.next==self.last):
            self.last=None
        else:
            current=self.last.next
            while current.next is not self.last:
                current=current.next
            current.next=self.last.next
            self.last=current

    # def delete_item(self,x):
    #     if self.is_Empty():
    #         print("Circular Link List is Empty")
    #         return
        
    #     if self.last.next == self.last:
    #         if self.last.item == x:
    #             self.last = None
    #             print(f"Deleted item: {x}")
    #         else:
    #             print("Item not found")
    #         return
        
    #     current=self.last.next
    #     while current is not self.last:
    #         if current.next.item==x:
    #             current.next=current.next.next
    #             if current.next==self.last:
    #                 self.last=current
    #             break
    #         current=current.next

    # def delete_item(self,x):
    #     if not self.is_Empty():
    #          if self.last.next==self.last:
    #              if self.last.item==x:
    #                  self.last=None
    #          else:
    #              if self.last.next.item==x:
    #                  self.delete_first()
    #              else:
    #                 current=self.last.next
    #                 while current is not self.last:
    #                     if current.next==self.last:
    #                         if self.last.item==x:
    #                             self.delete_last()
    #                             break
    #                     if current.next.item==x:
    #                         current.next=current.next.next
    #                         break                       
    #                     current=current.next
                    

                        
    def delete_item(self, x):
        if self.is_Empty():
            print("Circular Linked List is Empty")
            return

        # Case 1: Only one node
        if self.last.next == self.last:
            if self.last.item == x:
                self.last = None
            else:
                print("Item not found")
            return

        # Case 2: Delete first node
        if self.last.next.item == x:
            self.delete_first()
            return

        # Case 3: Delete any middle or last node
        current = self.last.next
        while current.next != self.last:
            if current.next.item == x:
                current.next = current.next.next
                return
            current = current.next

        # Case 4: Delete last node
        if self.last.item == x:                                                                                                                                                                                                     
            self.delete_last()
        else:
            print("Item not found")

    def __iter__(self):
        if self.last is None:
            return iterator(None) 
        else:
            return iterator(self.last.next)            

                    

class iterator:
    def __init__(self,start):
        self.current=start
        self.start=start
        self.count=0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current is None:
            raise StopIteration
        if self.current ==self.start and self.count==1:
           raise StopIteration
        else:
            self.count=1
        
        data=self.current.item
        self.current=self.current.next
        return data




c=CLL()
c.insert_at_start(30)
c.insert_at_start(20)
c.insert_at_start(10)
c.insert_at_start(0)
# print(c.search(60))
c.insert_at_last(40)
c.insert_After(c.search(0),25)

# current=c.last.next
# while current is not c.last:
#     print(current.item)
#     current=current.next

c.print_list()
for i in c:
    print(i,end=" ")
