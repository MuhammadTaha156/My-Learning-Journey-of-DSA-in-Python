
class Queue:
    def __init__(self):
        self.queue=[]
        self.rear=None
        self.front=None

    def is_empty(self):
        return len(self.queue)==0
    
    def enqueue(self,x):
        if self.is_empty():
            self.front=0
            self.rear=0
        else:
            
            self.rear+=1
        self.queue.append(x)

    def dequeue(self):
        if not self.is_empty():
            self.queue.pop(0)
            
        else:
            raise IndexError("Queue Underflow")

    def get_front(self):
        if not self.is_empty():
            return self.queue[self.front]
        else:
            raise IndexError("Queue Underflow")

    def get_rear(self):
        if not self.is_empty():
            if self.rear>=len(self.queue):
                self.rear-=1
            return self.queue[self.rear]
        else:
            raise IndexError("Queue Underflow")
        

    def size(self):
             return len(self.queue)
    
     
q=Queue()
try:
    print(q.get_front())
except IndexError as e:
    print(e.args[0])

q.enqueue(30)
q.enqueue(20)
q.enqueue(10)
print(q.queue)
print(q.get_front())
print(q.get_rear())
q.dequeue()
print(q.queue)
print(q.get_front())
print(q.get_rear())

print(q.size())






