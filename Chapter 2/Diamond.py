class A:
	def b(self):
		print("Comming from A")

class B(A):
	def b(self):
		print("Comming from B")
class C(A):
	def b(self):
		print("Comming from C")
		
class D(B,C):
	pass
