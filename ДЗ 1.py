# Создать программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, 
# является ли этот день выходным.
'''
N = int(input("Введите номер дня недели:  "))
if N == 6 or N == 7: print("Этот день выходной")
else: print("Этот день будний")
'''

# Напишите программу для проверки истинности утверждения для всех значений предикат
'''
for X in 0,1:
   for Y in 0,1:
       for Z in 0,1:
           if not(X or Y or Z) == (not(X) and not(Y) and not(Z)): print("Утверждение истинно")
           else: print("Утверждение ложно")
'''

# Напишите программу, которая принимает на вход координаты точки (X и Y, причем X и Y не равны 0)
# и выдает номер четверти плоскости, в которой находится эта точка
'''
x = int(input("Введите координату x: "))
y = int(input("Введите координату y: "))
if x>0 and y>0: print("точка находится в I четверти")
else: 
    if x<0 and y>0: print("точка находится во II четверти")
    else:
        if x<0 and y<0: print("точка находится в III четверти")
        else: print("точка находится в IV четверти")
'''

# Напишите программу, которая по заданному номеру четверти показывает диапазон возможных
# координат точек в этой четверти
'''
n = int(input("Введите номер четверти: "))
if n == 1: print("x>0, y>0")
else:
    if n == 2: print("x<0,y>0")
    else:
        if n == 3: print("x<0, y<0")
        else: print("x>0,y<0")
'''

# Напишите программу, которая принимает на вход координаты двух точек и находит 
# расстояние между ними в 2D пространстве
'''
x1 = int(input("Введите координату x первой точки: "))
y1 = int(input("Введите координату y первой точки: "))
x2 = int(input("Введите координату x второй точки: "))
y2 = int(input("Введите координату y второй точки: "))
L = float()
L = (((x2-x1)**2)+((y2-y1)**2))**0.5
print(L)
'''

