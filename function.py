#def hello(head,target):
#      if head == None:
#            print("list is empty")
#      else:
#            temp=head
#            while temp!=None:
#                  if temp == target:
#                        temp=temp.next.next
#                  else:
#                        temp=temp.next
#hello()   




def delNode(head, K):
    K=2
    # Code here
    temp =head
    while temp!=None:
        if temp == k:
             temp=temp.next
             temp=temp.next
        else:
             temp=temp.next
    return head

delNode(1,2,4,5)