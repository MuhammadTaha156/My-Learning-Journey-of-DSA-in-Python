class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next

class Queue:
    def __init__(self):
        self.rear=None
        self.front=None
        self.item_count=0

    def is_empty(self):
        return self.front==None

    def enqueue(self,x):
        n=Node(x)
        if self.is_empty():
            self.front=n
        else:
            self.rear.next=n
        self.rear=n
        self.item_count+=1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is underflow")
        elif self.front==self.rear:
            self.front=None
            self.rear=None
        else:
            self.front=self.front.next
        self.item_count-=1

    def get_front(self):
        if self.is_empty():
            raise IndexError("Stack is Underflow ")
        else:
            return self.front.item

    def get_rear(self):
        if self.is_empty():
            raise IndexError("Stack is Underflow ")
        else:
            return self.rear.item

    def size(self):
        return self.item_count
    
    def whole_queue(self):
        current=self.front
        while current is not None:
            print(current.item,end=" ")
            current=current.next
    

q=Queue()
try:
    print(q.get_front())
except IndexError as e:
    print(e.args[0])

q.enqueue(30)
q.enqueue(20)
q.enqueue(10)
q.whole_queue()
# print(q.get_front())
# print(q.get_rear())
# q.dequeue()
# print()
# print(q.get_front())
# print(q.get_rear())
# print(q.size())






