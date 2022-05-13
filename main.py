class Stack:
	def __init__(self):
		self.items = []  
  
	def is_empty(self):
		return self.items == []
  
	def push(self, item):
		self.items.insert(0, item)
	
	def pop(self):
		return self.items.pop(0)
	
	def stack(self):
		return self.items

def balanced(expression):
	s = Stack()
	for i in expression:
		if i == '(':
			s.push(i)
		if i == ')':
			if '(' in s.stack():
				s.pop()
			else:
				return False

	if not s.stack():
		return True
	else:
		return False
		
print(balanced(input()))