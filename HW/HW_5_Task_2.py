y = float(input('Enter Y : '))

def circle_radius(y):
	for x in range(-5,6):
		R = (x**2 + y**2) / 2 
		print( 'if x = ' , x , 'and y = ' , y , 'than radius = ', R)

circle_radius(y)

print()
print('---------------------------------------')
print()

z = float(input('Enter argument : '))

def z_square(z):
	for x in range(-5,6):
		Input = z**2 - x
		print(Input)

z_square(z)
