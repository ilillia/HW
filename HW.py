print('''
		1. Домашнее Задание №1
		2. Домашнее Задание №2
		3. Калькулятор''')
HomeWork = input('>>>')
#-----------------------------------#
if HomeWork == '1':
	print(''' 
			Домашнее Задание №1

			1. Задача 1
			2. Задача 2
			3. Задача 3
			4. Задача 4 (*)
	''')
	operation_1 = input('>>>')
	if operation_1 == '1':
		print('''
		--------------------------------------------------------
		Задача 1 - Найти площадь треугольника\
		 по формуле герона.
		--------------------------------------------------------
		''')
		print('	Введите последовательно все \
			три стороны треголька :')
		a1 = float(input('>>>'))
		b1 = float(input('>>>'))
		c1 = float(input('>>>'))
		d1 = float(2.00)
		e1 = float(0.5)
		p1 = float((a1 + b1 + c1) / d1)
		S1 = float((p1*(p1-a1)*(p1-b1)*(p1-c1)) ** e1)
		s1 = round(S1 , 1)
		print('Площадь треугольника ранвна', s1, 'См**2')
	elif operation_1 == '2':
		print('''
		--------------------------------------------------
		Задача 2 - Поменять местами значение 2 переменных.
		--------------------------------------------------
		''')
		a = 'Bad'
		b = 'Boy'
		print(a,b)
		
		print('=======')
		
		a , b = b , a 
		print(a,b)
	elif operation_1 == '3':
		print('''
		----------------------------------------------
		Задача 3 - Поменять местами значения двух 
		----------------------------------------------
		числовых переменных без использования третьей.
		----------------------------------------------
		''')
		a = 5
		b = 6
		print(a)
		print(b)

		print('=')

		b = b * a / b
		a = (a + a + a + a + a + a) / b

		print(round(a))
		print(round(b))
	elif operation_1 == '4':
		print('''
		--------------------------------------------------
		Задача 4 - Если число четное, вывести его квадрат,
		--------------------------------------------------
		а если нечетное - его удвоенное значение. (*)
		--------------------------------------------------
		''')
		x = float(input('Введите целое число '))
		x = round(x ** 2) if x // 2 == x / 2 else round(x * 2)
		print(x)
	else : print('Оно тебе не надо')
#-----------------------------------#
if HomeWork == '2':
	print('''
		1. Задание 1
		2. Задание 2
		3. Задание 3''')
	operation = input('>>>')
	if operation == '1':
		print('''
		---------------------------------
		Задание 1 - Программа Авторизцииы
		---------------------------------
		''')
		name = input('		Введите имя : ')
		password = input('		Введите пароль : ')
		if name == 'Anton' and password == '1':
			print('''
			{Четкий Пацан}''')
		elif name == 'ILLIA' and password == '2':
			print('''
			{Самый четкий пацан}''')
		elif name == 'PETR POROSHENKO' and password == '3':
			print('''
			{Тут и говорить нечего - \
		предводитель четких пацанов}''')
		elif name == 'Anton' or password == '1':
			print("		{Неверный логин или пароль}")
		elif name == 'ILLIA' or password == '2':
			print("		{Неверный логин или пароль}")
		elif name == 'PETR POROSHENKO' or password == '3':
			print("		{Неверный логин или пароль}")
		else : print('''
		Лох :)''')
	elif operation == '2':
		print('''
		------------------- 
		Задание 2 - Функция
		-------------------
		''')
		from math import (sin, cos, tan, atan, pi)
		PI = pi
		x = float(input('Укажите аргумент '))
		if  PI > x and x > -PI :
			y = cos(3*x) 
			print(y)
		elif x <= -PI or x >= PI :
			y = x
			print(round(y))
		else : print('Указаный аргумент\
		не пренадлежит функции ')
	elif operation == '3':
		print('''
		---------------------------------------------------
		Задача 3 - Нахождение корней \
		квадратного уравнения.
		---------------------------------------------------
		''')
		a = float(input('Укажите a '))
		b = float(input('Укажите b '))
		c = float(input('Укажите c '))
		D = float(b ** 2 - 4*a*c)
		X1 = (-b + D**0.5) / (2*a)
		X2 = (-b - D**0.5) / (2*a)
		if D > 0 :
			print('Корни :', round(X1), ';', round(X2))
		elif D == 0 :
			print('Корень:', round(X1))
		elif D < 0 : 
			print('Корней нет')
		else :
			print('Оно тебе не надо')
	else : print('Оно тебе не надо')
#-----------------------------------#
if HomeWork == '3':
		print(''' 
			  1. Прибавить
			  2. Отнять
			  3. Возведение в степень''')
		operation = input('>>>')
		if operation == '1':
			x1 = float(input('Введите первое число '))
			y1 = float(input('Введите второе число '))
			print(round(x1 + y1))
		elif operation == '2':
			x2 = float(input('Введите первое число '))
			y2 = float(input('Введите второе число '))
			print(round(x2 - y2))
		elif operation == '3' :
			x3 = float(input('Введите число '))
			y3 = float(input('Укажите степень '))
			print(round(x3 ** y3))
		else : 
				print('Оно тебе не надо')
#-----------------------------------#