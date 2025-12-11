class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next


class Deque:
    def __init__(self):
        self.front=None
        self.rear=None
        self.item_count=0

    def is_empty(self):
        return self.front==None
    
    def insert_front(self,x):
        n=Node(None,x,self.front)
        if self.is_empty():   
            self.rear=n
        else:
            self.front.prev=n
        self.front=n
        self.item_count+=1


    def insert_last(self,x):
        n=Node(self.rear,x,None)
        if self.is_empty():      
            self.front=n
        else:
            self.rear.next=n
        self.rear=n
        self.item_count+=1

    def delete_front(self):
        if self.is_empty():
            raise IndexError("Deque is Empty")
        elif self.front==self.rear:
            self.front=None
            self.rear=None
        else:
            self.front=self.front.next
            self.front.prev=None
        self.item_count-=1

    def delete_rear(self):
        if self.is_empty():
            raise IndexError("Deque is Empty")
        elif self.front==self.rear:
            self.front=None
            self.rear=None
        else:
            self.rear=self.rear.prev
            self.rear.next=None
        self.item_count-=1

    def get_front(self):
        if self.is_empty():
            raise IndexError("Deque is Empty")
        else:
            return self.front.item
        
    def get_rear(self):
        if self.is_empty():
            raise IndexError("Deque is Empty")
        else:
            return self.rear.item

    def size(self):
        return self.item_count
    
    def whole_deque(self):
        current=self.front
        while current is not None:
            print(current.item,end=" ")
            current=current.next
    
d=Deque()

d.insert_front(30)
d.insert_front(60)
d.insert_last(50)
d.insert_last(90)
d.whole_deque()
print()

print(d.get_front())
print(d.get_rear())
print()

d.delete_front()
# d.delete_rear()

d.whole_deque()
print()

print(d.get_front())
print(d.get_rear())
print(d.size())
