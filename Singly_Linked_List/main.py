class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next


class SLL:
    def __init__(self,start=None):
        self.start=start

    def is_Empty(self):
        if  self.start ==None:
            print("LinkList is Empty")
            return self.start== None
        

    def insert_at_start(self,x):
        if not self.is_Empty():
            n=Node(x,self.start)
            self.start=n
            print("Node is Added to SLL")
        else:
            n=Node(x)
            self.start=n
            print("Insert at Start\n")
    

    def insert_at_last(self,x):
        if not self.is_Empty():
            n=Node(x)
            current=self.start
            while current.next is not None:
                current=current.next
            current.next=n
        else:
            n=Node(x)
            self.start=n


    def search(self,x):
        current=self.start
        if self.is_Empty():
            pass
        else:
            while current is not None:
                if current.item==x:
                    print(f"\nFound {x}")
                    return current
                current=current.next



    def insert_After(self,N,x):
        if self.start==N:
            n=Node(x,self.start.next.next)
            self.start.next=n
        else:
            current=self.start
            while current is not None:
                if current==N:
                    n=Node(x,current.next)
                    current.next=n
                current=current.next


    def print_List(self):
        current=self.start
        while current is not None:
            print(current.item,end=" ")
            
            current=current.next
        print("\n")


    def delete_first(self):
        if self.start is not None:
            self.start=self.start.next


    def delete_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start=None
        else:
            current=self.start
            while current is not None:
                if current.next.next==None:
                    current.next=None
                current=current.next


    def delete_item(self,x):
        if self.start==None:
            pass
        elif self.start.next is None:
            if self.start.item==x:
                self.start=None
        else:
            current=self.start
            if current.item==x:
                self.start=current.next
            while current is not None:
                if current.next.item==x:
                    current.next=current.next.next
                    break
                current=current.next


    def __iter__(self):
        return iterator(self.start)


class iterator:
    def __init__(self,start):
        self.current=start

    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.current:
            raise StopIteration
        else:
            data=self.current.item
            self.current=self.current.next
            return data



# s1=SLL()


# s1.insert_at_start(10)
# s1.insert_at_last(20)
# s1.insert_at_last(30)
# s1.insert_at_last(40)
# s1.insert_at_last(50)

# # current=s1.start

# # while current is not None:
# #     print(current.item)
# #     current=current.next

# s1.print_List()


# s1.search(20)

# s1.insert_After(s1.search(30),35)
# s1.print_List()

# s1.delete_item(35)
# s1.print_List()



# for i in s1:
#     print(i)