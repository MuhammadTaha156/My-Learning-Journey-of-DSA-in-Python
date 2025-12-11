class Stack:
    def __init__(self):
        self.items=[]

    def is_Empty(self):
        return len(self.items)==0
    
    def push(self,x):
        self.items.append(x)

    def pop(self):
        if not self.is_Empty():
            return self.items.pop()
        else:
            raise IndexError(" Stack is Empty ")
    
    def peek(self):
        if not self.is_Empty():
            return self.items[-1]
        else:
            raise IndexError(" Stack is Empty ")
         

    def size(self):
        return len(self.items)
    
s1=Stack()
s1.push(10)
s1.push(20)
s1.push(30)
print(s1.peek())
print(s1.size())
print(s1.items)
print(s1.pop())
print(s1.items)
    
