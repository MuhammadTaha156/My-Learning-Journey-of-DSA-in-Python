


class Queue:
    def __init__(self):
        self.queue=[]
        self.rear=-1
        self.front=-1
    
    def is_empty(self):
        return len(self.queue)==0
    
    def enqueue(self,x):
        if self.is_empty():
            self.rear+=1
            self.front+=1
            self.queue.append(x)
        else:
            self.rear+=1
            self.queue.append(x)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is Underflow")
        else:
            self.front+=1
            self.queue=self.queue[1:]

    def get_front(self):
        return self.front
    
    def get_rear(self):
        return self.rear
    
    def size(self):
        return len(self.queue)
    
    

q=Queue()
q.enqueue(30)
q.enqueue(20)
q.enqueue(10)

print(q.queue)
q.dequeue()
print(q.queue)
print(q.get_front())
print(q.get_rear())
print(q.size())


