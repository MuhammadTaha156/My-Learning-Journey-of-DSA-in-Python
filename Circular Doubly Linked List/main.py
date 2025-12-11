class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next

class CDLL:
    def __init__(self,start=None):
        self.start=start

    def is_Empty(self):
        return self.start==None
    
    def insert_at_start(self,x):
        
        if self.is_Empty():
            n=Node(None,x,None)
            n.next=n
            n.prev=n                     
            self.start=n
        else:
            n=Node(self.start.prev,x,self.start)
            self.start.prev.next=n
            self.start.prev=n
            self.start=n
    
    def insert_at_last(self,x):
        if self.is_Empty():
            n=Node(self.start,x,self.start)
            self.start=n
        else:
            n=Node(self.start.prev,x,self.start)
            self.start.prev.next=n
            self.start.prev=n


    def search(self,x):
        if self.is_Empty():
            print("Link List is Empty")
        else:
            current=self.start
            while current is not self.start.prev:
                if current.item ==x:
                    print(f"{current.item } Found")
                    return current
                current=current.next

    
    def insert_after(self,N,x):
        if self.is_Empty():
            print("Link List is Empty")
            pass
        if N is not None:
            n=Node(N,x,N.next)
            N.next.prev=n
            N.next=n       
   
    def print_list(self):
        if self.is_Empty():
            print("Link List is Empty")
        else:
            current=self.start
            while current is not self.start.prev:
                print(current.item,end=" " )                   
                current=current.next
            print(current.item)

    def delete_first(self):
        if self.is_Empty():
            print("Link List is Empty")
        else:
            if self.start.next==self.start:
                self.start=None
            else:
                self.start.prev.next=self.start.next
                self.start.next.prev=self.start.prev
                self.start=self.start.next

    def delete_last(self):
        if self.is_Empty():
            print("Link List is Empty")
        else:
            if self.start.next==self.start:
                self.start=None
            else:
                self.start.prev.prev.next=self.start
                self.start.prev=self.start.prev.prev


    def delete_item(self,x):
        if self.is_Empty():
            print("Link List is Empty")
            return
        if self.start.next==self.start:
            if self.start.item==x:
                self.start=None
            else:
                print("Item not found")
            return
        
        
        current=self.start
        while current.next is not self.start:
            if current.item ==x:
                                       
                    current.prev.next=current.next
                    current.next.prev=current.prev
                    if current==self.start:
                        self.start=current.next
            current=current.next
        if current.item ==x:
                current.prev.next=current.next
                current.next.prev=current.prev


    def __iter__(self):
        return CDLL_iterator(self.start)


class CDLL_iterator:
    def __init__(self,start):
        self.current=start
        self.start=start
        self.count=0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current is None:
            raise StopIteration
        if self.current==self.start and self.count==1:
            raise StopIteration
        else:
            self.count=1
        data=self.current.item
        self.current=self.current.next
        return data


cd=CDLL()
cd.insert_at_start(30)
cd.insert_at_start(20)
cd.insert_at_start(10)
cd.insert_at_start(0)
cd.insert_at_last(40)
cd.insert_at_last(50)
# cd.search(40)
cd.insert_after(cd.search(40),45)
cd.print_list()
print()
print("Delete First")
cd.delete_first()
cd.print_list()
print()
print("Delete last")
cd.delete_last()
cd.print_list()
print()
print("Delete item")
print("Delete item")
cd.delete_item(20)
cd.print_list()
print()

print("Iteration" )
for i in cd:
    print(i,end=" ")


