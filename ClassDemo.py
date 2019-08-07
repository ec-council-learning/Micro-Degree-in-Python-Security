class Singleton(object):
	ClassVariable = 99
	def __init__(self):
		self.InstanceVariable = 88
		self.__hidden = -1
	def __new__(cls):
		if not hasattr(cls,'instance'):
			cls.instance = super(Singleton, cls).__new__(cls)
		return cls.instance

	@property
	def hidden(self):
		return self.__hidden
	
	@hidden.setter
	def hidden(self, value):
		self.__hidden = value

	@classmethod
	def class_method(cls):
		print("I am a class method, I can be called without an instance!")
	@staticmethod
	def static_method(a = 10):
		print("Im a static method, I can be called from class and instance!")

	def __str__(self):
		return f"I am the __str__ : {self.__class__.__name__}"

	def __repr__(self):
		return f"I am the __repr__: {self.__class__}"