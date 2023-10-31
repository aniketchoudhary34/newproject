class stack:
    def __init__(self):
        self.items = []
    def push(self,item):
        return self.items.append(item)
    def pop(self):
        if not self.isempty():
            return self.items.pop()
        else:
            return "empty stack"
    def isempty(self):
        return len(self.items) == 0
    def size(self):
        return len(self.items)
    def peek(self):
        if not self.isempty():
            return self.items[-1]
        else:
            return "empty stack"
stacks =stack()
stacks.push(0)                
stacks.push(1)
stacks.push(2)
stacks.push(3)
stacks.push(4)


print(stacks.size())
print(stacks.peek())
popped_items = stacks.pop()
print(popped_items)
print(stacks.size())
print(stacks.peek())


stack1 = stack()
print(stack1.size())
popped_items = stack1.pop()
print(popped_items)