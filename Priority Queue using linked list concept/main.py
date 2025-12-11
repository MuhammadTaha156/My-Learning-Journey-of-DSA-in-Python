class Node:
    def __init__(self,item=None,priority=None,next=None):
        self.item=item
        self.priority=priority
        self.next=next
class priority_Queue:
    def __init__(self,start=None):
        self.start=start
        self.itemCount=0

    def is_empty(self):
        return self.start==None
    
    def push(self,x,p):
        n=Node(x,p,None)
        if not self.start or p<self.start.priority:
            n.next=self.start
            self.start=n
        else:
            current=self.start
            while current.next is not None and current.next.priority>p:
                current=current.next
            n.next=current.next
            current.next=n
        self.itemCount+=1
                
                 
    def pop(self):
        if self.is_empty():
            raise IndexError("Queue is Empty")
        else:
            self.itemCount-=1
            data=self.start.item
            self.start=self.start.next
            return data  


    def size(self):
        return self.itemCount
    

    def whole_queue(self):
        current=self.start
        while current is not None:
            print(current.item,"-",current.priority,end=" | ")
            current=current.next


pq=priority_Queue()
try:
    pq.pop()
except IndexError as e:
    print(e.args[0])
pq.push(30,4)
pq.push(60,8)
pq.push(10,9)
pq.push(80,2)
pq.whole_queue()
print()
print(pq.pop())
pq.whole_queue()
print()
print(f"Size of Queue:  ",pq.size())


