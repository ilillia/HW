
while preference == 'continue':

def plus_function(a,b):
	   output = '{} + {} = {}'
	   plus_function = output.format(a, b, a + b)
	   return plus_function
       preference = input('''if you want to continue than print it
if not write : exit 
>>> ''')
    
def minus_function(a,b):
	   output = '{} - {} = {}'
	   minus_function = output.format(a, b, a - b)
	   return minus_function
       preference = input('''if you want to continue than print it
if not write : exit 
>>> ''')
    
def divide_function(a,b):
        output = '{} / {} = {}'
        divide_function = output.format(a, b, a / b)
        return divide_function
        preference = input('''if you want to continue than print it
    if not write : exit 
    >>> ''')
    
def multiply_function(a,b):
        output = '{} * {} = {}'
        multiply_function = output.format(a, b, a * b)
        return multiply_function
        preference = input('''if you want to continue than print it
    if not write : exit 
    >>> ''')
     
def input_values():
        returned_values = {}
        first_number  = float(input('Enter First Number >>> '))
        type_of_operation  = input('Enter Base Function >>> ')
        second_number  = float(input('Enter Second Number >>> '))
    
        returned_values['first_number'] = first_number
        returned_values['operation'] = type_of_operation
        returned_values['second_number'] = second_number
    
        return returned_values
        
def main():
        print()
        print('''Base functions :  +  ,  -  ,  *  ,  //

                // - integer division ''')
        print()

        entry_value = input_values()

        print()
        print(entry_value)
        print()

        a = entry_value['first_number']
        b = entry_value['second_number']

        if entry_value['operation'] == '+':
    	   print(plus_function(a,b))
        elif entry_value['operation'] == '-':
    	   print(minus_function(a,b))
        elif entry_value['operation'] == '/' and b != 0 :
    	   print(divide_function(a,b))
        elif entry_value['operation'] == '*':
    	   print(multiply_function(a,b))
        elif entry_value['operation'] == '//' and b != 0 :
            print(integer_division_function(a,b))
        else :
    	   print('Incorrect input')
    
main()
while else :
    break