class Node:
    def __init__(self,data,pointer):
        self.data=data
        self.pointer=pointer

class LinkedList:
        
    def __init__(self,head):
        self.head=None

    
        
    def Insert(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
        else:
            cur=self.head
            while (cur.pointer is not None):
                cur=cur.pointer
            cur.pointer=newnode



   

if __name__ == "__main__":
    dummy=Node(10)
    dummy4=Node(20)
    dummy1=Node(30)
    dummy2=Node(10)
    print(dummy.data)
    print(dummy4.data)
    print(dummy1.data)

    print(dummy2.pointer)
