class node(object):
    def __init__(self,val):
        self.data=val
        self.next=None

class LinkedList(object):
    def __init__(self):
        self.head=None
        self.len=0
    
    def Create(self):
        n=int(input("Enter Number of Elements in Linked List : "))
        if(n>0):
            val=int(input("Enter Element 1 : "))
            self.head=node(val)
            temp=self.head
            self.len+=1
            for i in range(1,n):
                val=int(input(f"Enter Element {i+1} : "))
                new_node=node(val)
                temp.next=node(val)
                temp=temp.next
                self.len+=1
        self.Display()

    def __len__(self):
        return self.len
    
    def insert_at_head(self):
        val=int(input("Enter Element : "))
        new_node=node(val)
        new_node.next=self.head
        self.head=new_node
        self.len+=1
        self.Display()

    def insert_at_tail(self):
        val=int(input("Enter Element : "))
        new_node=node(val)
        if(self.head==None):
            self.head=new_node
        else:
            temp=self.head
            for i in range(self.len-1):
                temp=temp.next
            temp.next=new_node
        self.len+=1
        self.Display()       

    def insert_at_middle(self):
        while(True):
            index=int(input(f"Enter Index Between 2 and {self.len-1} : ")) #3 len = 4
            if(index < self.len and index > 1 ):
                val=int(input("Enter Element : "))
                new_node=node(val)
                temp=self.head
                for i in range(1,index-1):#node1 . node2 . node3 . node4
                    temp=temp.next
                new_node.next=temp.next
                temp.next=new_node
                self.len+=1
                self.Display()
                break
            else:
                print("Out of Index Range") 

    def clear(self):
        self.head=None
        self.len=0
        self.Display()

    def delete_from_head(self):
        if(self.head==None):
            print("Empty List")
        else:
            self.head=self.head.next
            self.len-=1
            self.Display()

    def delete_from_tail(self):
        if(self.head==None):
            print("Empty List")
        elif(self.len==1):
            self.head=None
            self.len=0
        else:
            temp=self.head
            for i in range(1,self.len-1):
                temp=temp.next
            temp.next=None
            self.len-=1
        self.Display()
    
    def delete_by_value(self):
        val=int(input("Enter Element : "))
        count=0
        temp=self.head
        if self.head and val == self.head.data:
            self.head=self.head.next
            count=1
            self.len-=1
        if(self.head):
            while(temp.next != None):
                if(temp.next.data == val):
                    count=1
                    temp.next=temp.next.next
                    self.len-=1
                else:
                    temp=temp.next

        if(count == 0):
            print("Element Not Found")

        self.Display()

    def delete_by_index(self):
        while(True):
            index=int(input(f"Enter Index Between 1 and {self.len} : "))
            if(index==1):
                self.delete_from_head()
                break
            elif(index==self.len):
                self.delete_from_tail()
                break
            elif(index > 1 and index < self.len):
                temp=self.head
                for i in range(1,index-1):
                    temp=temp.next
                temp.next=temp.next.next
                self.len-=1
                self.Display()
                break
            else:
                print("Index Out of range")

    def search_by_value(self):
        val=int(input("Enter Element : "))
        count=0
        temp=self.head
        for i in range(self.len):
            if(temp.data == val):
                count+=1
                print(f"Found At Index {i+1}")
            temp=temp.next
        if(count == 0):
            print("Element Not Found")

    def search_by_index(self):
        while(True):
            index=int(input(f"Enter Index Between 1 and {self.len} : "))
            if(index <= self.len and index > 0):
                temp=self.head
                for i in range(1,index):
                    temp=temp.next
                print(f"Element at Index {index} : {temp.data} ")
                break
            else:
                print("Index Out Of Range")



    def Display(self):
        temp=self.head
        print("Linked List :",end=' ')
        for i in range(self.len):
            print(f"{temp.data}",end=" -> ")
            temp=temp.next
        print("None")
