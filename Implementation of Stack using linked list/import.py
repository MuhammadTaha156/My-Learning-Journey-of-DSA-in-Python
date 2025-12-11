import sys
sys.path.append(r'D:\COURSES Practices\DSA with Python')
from Singly_Linked_List.main import *

class Stack:
    def __init__(self):
        self.items=SLL()
        self.item_Count=0


    def is_empty(self):
        return self.items.is_Empty()


    def push(self,x):
        self.items.insert_at_start(x)
        self.item_Count+=1


    def pop(self):
        if not self.is_empty():
            self.items.delete_first()
            self.item_Count-=1
        else:
            raise IndexError("Stack is Empty")


    def peek(self):
        if not self.is_empty():
            return self.items.start.item
        else:
            raise IndexError("Stack is Empty")
        
    

    def size(self):
        return self.item_Count
    
    def display_Stack(self):
        return self.items.print_List()


s=Stack()
s.push(30)
s.push(20)
s.push(10)
print(s.peek())
print(s.size())
print(s.display_Stack())
s.pop()
print(s.display_Stack())
