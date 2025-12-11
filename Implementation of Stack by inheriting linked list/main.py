import sys
sys.path.append(r'D:\COURSES Practices\DSA with Python')
from Singly_Linked_List.main import *


class Stack(SLL):
    def __init__(self, start=None):
        super().__init__(start)
        self.item_Count=0
    
    def is_Empty(self):
        return super().is_Empty()
    
    def push(self,x):
        super().insert_at_start(x)
        self.item_Count+=1

    def pop(self):
        if not self.is_Empty():
            self.item_Count-=1
            return super().delete_first()
        else:
            raise IndexError("Stack is Empty")
        
    def peek(self):
        if not self.is_Empty():
            return self.start.item
        else:
            raise IndexError("Stack is Empty")
        
    def size(self):
        return self.item_Count
    
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




