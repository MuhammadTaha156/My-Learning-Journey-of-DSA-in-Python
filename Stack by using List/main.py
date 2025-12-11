class stack:
    def __init__(self):
        self.stack=[]

    def is_empty(self):
        return len(self.stack)==0
        
    def push(self,x):
        self.stack.append(x)

    def pop(self):
        if self.is_empty():
            raise IndexError(" Stack is Empty ")
        else:
            self.stack.pop()


    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError(" Stack is Empty ")
        
    def size(self):
        return f"Length of Stack is {len(self.stack)}"


s=stack()
s.push(30)
s.push(20)
s.push(10)
print(s.stack)
s.pop()
s.pop()
print(s.stack)
print(s.peek())
print(s.size())

