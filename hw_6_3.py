'Задание №3'

class DifferentTypeError(Exception):
	def __init__(self, set_of_types):
		self.set_of_types = set_of_types

def check_params_type(*args):
	set_of_types = set()

	for elem in args:
		set_of_types.add(type(elem))

	if len(set_of_types) > 1:
		print('Not Successful')
		raise DifferentTypeError(set_of_types)

	return set_of_types

def main(*args):
	try:
		print()
		check_params_type(*args)
		print('Successful')

	except DifferentTypeError as error:
		print('Error : too many types', error)
	finally:
		for element in args:
			print("Element '{}' type {}.".format(element,type(element)))

if __name__ == '__main__':
	main(1,2,3)
	main('w','o','r','k','i','n','g','?')
	main(1,'lol',True,12.34,[12,34],(22.33))

