class Stack(list):
    def is_empty(self):
        return len(self)==0
    
    def push(self,x):
        self.append(x)

    def pop(self):
        if not self.is_empty():
            return super().pop()
        else:
            raise IndexError("Stack is Empty")
        
    def peek(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError("Stack is Empty")

    def size(self):
        return len(self)
    
    def insert(self,index,data):
        raise IndexError("Cannot Insert between Stack")

    
s=Stack()
s.push(10)
s.push(20)
s.push(30)
print(s)
s.pop()
print(s)
print(s.peek())
print(s.size())












