import sys
sys.path.append(r'D:\COURSES Practices\DSA with Python')
from Singly_Linked_List.main import *



class stack:
    def __init__(self):
        self.List=SLL()
        self.item_Count=0

    def is_empty(self):
        return self.List.is_Empty()
    
    def push(self,x):
        self.List.insert_at_start(x)
        self.item_Count+=1

    def pop(self):
        if not self.is_empty():
            self.List.delete_first()
            self.item_Count-=1
        else:
            raise IndexError("Stack is Empty")
        
    def peek(self):
        if not self.is_empty():
            return self.List.start.item
        else:
            raise IndexError("Stack is Empty")

        
    def size(self):
        return self.item_Count
    
    def print_List(self):
        return self.List.print_List()
    
s=stack()
s.push(30)
s.push(20)
s.push(10)
print(s.print_List())
s.pop()
print(s.print_List())
print(s.peek())
print(s.size())










