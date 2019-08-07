import Shelve

my_dict = {'a':1,'b':2,'c':3}
my_list = [1,2.0,3e4,'string']
class Shelved(object):
	def __init__(self, name):
		self.__name = name

file = shelve.open('shelved_objects.shelve', protocol = 2)
file['class'] = Shelved('ECCouncil')
file['li'] = my_list
file['di'] = my_dict
file.close()
