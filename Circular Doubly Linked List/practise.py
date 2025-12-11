class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next

class CDLL:
    def __init__(self,start=None):
        self.start=start

    def is_Empty(self):
        return self.start==None
    
    def insert_at_start(self,x):
        if self.is_Empty():
            n=Node(None,x,None)
            n.next=n
            n.prev=n       
        else:
            n=Node(self.start.prev,x,self.start)
            self.start.prev.next=n
            self.start.prev=n
        self.start=n

    def insert_at_last(self,x):
        if self.is_Empty():
            n=Node(self.start,x,self.start)
            self.start=n
        else:
            n=Node(self.start.prev,x,self.start)
            self.start.prev.next=n
            self.start.prev=n

    def search(self, x):
        if self.start is None:
            return None

        current = self.start

        while True:
            if current.item == x:
                return current

            current = current.next

            if current is self.start:
                break

        return None

    def insert_after(self,N,x):
        if self.is_Empty():
            print("Link List is Empty")
            return
        if N is not None:
            n=Node(N,x,N.next)
            N.next.prev=n
            N.next=n 


    def print_list(self):
        current=self.start
        if current is not None:
            print(current.item,end=" ")
            current=current.next
        while current is not self.start:
            print(current.item,end=" ")
            current=current.next


    def delete_first(self):
            if self.is_Empty():
                print("Link List is Empty")
            else:
                if self.start.next==self.start:
                    self.start=None
                else:
                    self.start.prev.next=self.start.next
                    self.start.next.prev=self.start.prev
                    self.start=self.start.next

    def delete_last(self):
        if self.start is None:
            print("Linked List is Empty")
            return

        # Only one node
        if self.start.next == self.start:
            self.start = None
            return

        # More than one node
        last = self.start.prev
        second_last = last.prev

        second_last.next = self.start
        self.start.prev = second_last



    def delete_item(self,x):
        if self.is_Empty():
            print("Link List is Empty")
            return
        if self.start.next==self.start:
            if self.start.item==x:
                self.start=None
            else:
                print("Item not found")
            return
        
        
        current=self.start
        while current.next is not self.start:
            if current.item ==x:
                                       
                    current.prev.next=current.next
                    current.next.prev=current.prev
                    if current==self.start:
                        self.start=current.next
            current=current.next
        if current.item ==x:
                current.prev.next=current.next
                current.next.prev=current.prev

    def __iter__(self):
        return CDLLiterator(self.start)
                

class CDLLiterator:
    def __init__(self,start):
        self.current=start
        self.start=start
        self.count=0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current is None:
            raise StopIteration
        if self.current==self.start and self.count==1:
            raise StopIteration
        else:
            self.count=1
        data=self.current.item
        self.current=self.current.next
        return data


            
 

CD=CDLL()
CD.insert_at_start(20)
CD.insert_at_start(10)
CD.insert_at_last(30)
CD.insert_at_last(40)
CD.insert_after(CD.search(30),35)

# CD.print_list()
for i in CD:
    print(i,end=" ")





