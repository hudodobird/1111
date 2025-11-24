class stack:
    def __init__(self):
            self.items = []

    def isEmpty(self):
          if not self.items:
                return True
          else:
                return False
          
    def push(self, item):
          self.items.append(item)

    def remove(self):
          return self.items.pop()
    
    def peek(self):
          return self.items[-1]
    
    def size(self):
          return len(self.items)
    
    def __str__(self):
          return str(self.items)
    


s = stack()

s.push(4)
s.push('dog')
s.push(True)
print(s.items)
print(s.peek())
print(s.size())
print(s.isEmpty())
s.remove()
s.remove()
s.remove()
print(s.isEmpty())
print(s.items)