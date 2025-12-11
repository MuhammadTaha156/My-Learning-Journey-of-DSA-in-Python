class Deque:
    def __init__(self):
        self.deque=[]
        

    def is_empty(self):
        return len(self.deque)==0
    
    def insert_front(self,x):
        self.deque.insert(0,x)
        

    def insert_rear(self,x):
        self.deque.append(x)
        


    def delete_front(self):
        if self.is_empty():
            raise IndexError("Deque is Empty")
        else:
            self.deque.pop(0) 
            
    

    def delete_rear(self):
        if self.is_empty():
            raise IndexError("Deque is Empty")
        else:
            self.deque.pop()
            

    
    def get_front(self):
        if self.is_empty():
            raise IndexError("Deque is Empty")
        else:
            return self.deque[0]
        
    
    def get_rear(self):
        if self.is_empty():
            raise IndexError("Deque is Empty")
        else:
            return self.deque[-1]


    def size(self):
        return len(self.deque)
    
d=Deque()
d.insert_front(10)
d.insert_front(20)
d.insert_rear(30)
print(d.deque)
print(d.get_front())
print(d.get_rear())
print()
print(d.delete_front())
print(d.delete_rear())
print(d.deque)
print()
print(d.size())



