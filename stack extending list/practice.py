class Stack(list):
    def is_empty(self):
        return len(self)==0
    
    def push(self,x):
        self.append(x)

    def pop(self):
        if not self.is_empty():
            return super().pop()
        else:
            raise IndexError("Stack is EMpty")
        
    def peek(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError("Stack is EMpty")

    def size(self):
        return len(self)   


    def insert(self,index,data):
        raise AttributeError("No Attribute 'insert' in Stack")  

    


s=Stack()
s.push(30)
s.push(20)
s.push(10)
print(s)
print(s.peek())
s.pop()
print(s.size())
print(s)
# s.insert(1,34)





