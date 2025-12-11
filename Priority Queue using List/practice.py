class priority_Queue:
    def __init__(self):
        self.PQ=[]

    def push(self,x,p):
        index=0
        while index<len(self.PQ) and self.PQ[index][1]<p:
            index+=1
        self.PQ.insert(index,(x,p))

    def is_empty(self):
        return len(self.PQ)==0

    
    def pop(self):
        if self.is_empty():
            raise IndexError("Queue is Empty")
        else:
            return self.PQ.pop(0)[0]

    def size(self):
        return len(self.PQ)

pq=priority_Queue()
try:
    pq.pop()
except IndexError as e:
    print(e.args[0])
pq.push(30,4)
pq.push(60,8)
pq.push(10,9)
pq.push(80,2)
print(pq.PQ)
print(pq.pop())
print(pq.PQ)
print(pq.size())