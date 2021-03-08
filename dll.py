class node:
	def __init__(self, data): 
		self.data=data 
		self.next=None
		self.prev=None
class ll: 
	def __init__(self): 
		self.head=None
	# add at front
	def add1(self,data):
		new=node(data)
		if self.head:
			new.next=self.head
			self.head.prev=new
			self.head=new
		else:	
			self.head=new
	# insert at a given point
	def add2(self,data1,data2):
		new=node(data1)
		x=self.head
		while x.data!=data2:
			x=x.next
		y=x.next
		x.next=new
		new.prev=x
		new.next=y
		y.prev=new
	# insert at last
	def add3(self,data):
		new=node(data)
		x=self.head
		while x.next:
			pre=x
			x=x.next
		x.next=new
		new.prev=x
	#del from front
	def del1(self):
		x=self.head
		y=self.head.next
		y.prev=None
		self.head=y
		del x
	# del from given postion or value or node
	def del2(self,data):
		temp=self.head
		while temp.data!=data:
			temp=temp.next
		val=temp.next
		pre=temp.prev
		pre.next=val
		val.prev=pre
		del temp
	#del form last
	def del3(self):
		x=self.head
		while x:
			temp=x
			x=x.next
		val=temp.prev
		val.next=None
		del temp
	def rev(self):
		x=self.head
		while x:
			temp=x.prev
			x.prev=x.next
			x.next=temp
			x=x.prev
		self.head=temp.prev
	def trav(self):
		x=self.head
		pre=None
		while x:
			print(x.data,end=" ")
			pre=x
			x=x.next
		print()
		while pre:
			print(pre.data,end=" ")
			pre=pre.prev
		print("\n")
l=ll() 
l.add1(1) 
l.add1(2) 
l.add1(3) 
print("Add at front ")
l.trav()
l.add2(4,2)
print("Add at given")
l.trav()
l.add3(5)
l.add3(7)
print("Add at last")
l.trav()
"""l.del1()
print("del from front")
l.trav()
l.del2(4)
print("del the given node")
l.trav()
l.del3()
print("del the last node")
l.trav()
l.rev()
print("Reversed DLL")
l.trav()
"""
