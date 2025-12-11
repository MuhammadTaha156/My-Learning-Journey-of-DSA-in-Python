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
            self.last=n
            n.next=self.last
        else:
            n.next=self.last.next
            self.last.next=n

    def insert_at_last(self,x):
        n=Node(x)
        if self.is_Empty():
            self.last=n
            n.next=self.last
        else:
            n.next=self.last.next
            self.last.next=n
            self.last=n

    def search(self,x):
        if self.is_Empty():
            print("LinkList is Empty\n")
            return None
        current=self.last.next
        while current is not self.last:
            if current.item==x:
                print(f"{current.item} Found\n")
                return current
            current=current.next
        if current.item==x:
            print(f"{current.item} Found\n")
            return current
        return None
           


    def insert_after(self,N,x):
        if self.is_Empty():
            print("Linklist is Empty")
        else:
            if N is not None:
                n=Node(x,N.next)
                n.next=n
                if N==self.last:
                    self.last=n

    
    def print_list(self):
        if not self.is_Empty():
            current=self.last.next
            while current is not self.last:
                print(current.item,end=" ")
                current=current.next
            print(current.item,end=" ")


    def delete_first(self):
        if self.is_Empty():
            print("Link List is Empty\n")
        else:
            if self.last.next==self.last:
                self.last=None
            else:
                self.last.next=self.last.next.next


    def delete_last(self):
        if self.is_Empty():
            print("Link List is Empty\n")
        elif(self.last.next==self.last):
            self.last=None
        else:
            current=self.last.next
            while current.next is not self.last:
                current=current.next
            current.next=self.last.next
            self.last=current


    def delete_item(self,x):
        if self.is_Empty():
            print("Circular Linked List is Empty")
            return
        if self.last.next==self.last:
            if self.last.item==x:
                self.last=None
            else:
                print("Item not found")
            return
        if self.last.next.item==x:
            self.delete_first()
            return
        
        current=self.last.next
        while current.next is not self.last:
            if current.next.item==x:
                current.next=current.next.next
                return
            current=current.next

        if self.last.item==x:
            self.delete_last()
        else:
            print("Item not found")

    def __iter__(self):
        if self.last==None:
            return CLLiterator(None)
        else:
            return CLLiterator(self.last.next)


class CLLiterator:
    def __init__(self,start=None):
        self.current=start
        self.start=start
        self.count=0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current==None:
            raise StopIteration
        if self.current==self.start and self.count==1:
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
c.insert_at_last(40)
c.insert_at_last(50)
c.insert_at_last(60)
# c.print_list()
# print()
# c.delete_item(50)
# c.print_list()
# print()
# c.delete_first()
# c.print_list()
# print()
# c.delete_last()
# c.print_list()

for i in c:
    print(i,end=" ")

