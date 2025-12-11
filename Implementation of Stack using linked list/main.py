class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next

class Stack:
    def __init__(self,start=None):
        self.start=start
        self.item_count=0

    def is_empty(self):
        return self.start==None
    
    def push(self,x):
            n=Node(x,self.start)
            self.start=n
            self.item_count+=1

    def pop(self):
         if not self.is_empty():
              self.start=self.start.next
              self.item_count-=1
         else:
              raise IndexError("Stack is Empty")
         
    def peek(self):
         if not self.is_empty():
              return self.start.item
         else:
              raise IndexError("Stack is Empty")
         
    def size(self):
         return self.item_count
    
    def print_stack(self):
         current=self.start
         while current is not None:
              print(current.item,end=" ")
              current=current.next
        

s=Stack()
s.push(30)
s.push(20)
s.push(10)
s.print_stack()
s.pop()
s.print_stack()
print(s.peek())
print(s.size())





