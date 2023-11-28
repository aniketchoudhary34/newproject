def hello(head,target):
      if head == None:
            print("list is empty")
      else:
            temp=head
            while temp!=None:
                  if temp == target:
                        temp=temp.next.next
                  else:
                        temp=temp.next
hello()   

n=[1,2,3,4,5]
i=0
while i<n:
    print(i)