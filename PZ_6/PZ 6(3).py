# Дано множество A из N точек (N > 2, точки заданы своими координатами x, у). 
# Найти наибольший периметр треугольника, вершины которого принадлежат различным точкам множества A,
# и сами эти точки (точки выводятся в том же порядке, в котором они перечислены при задании множества A).
# Расстояние R между точками с координатами (x1, y1) и (x2, у2) вычисляется по формуле: R = √(x2 – x1)2 + (у2 – y1)2.
# Для хранения данных о каждом наборе точек следует использовать по два список: первый список для хранения абсцисс, второй — для хранения ординат.
import math
from itertools import combinations

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

N = int(input("Введите количество точек (N > 2): "))
if N < 2:
    print("Количество точек должно быть меньше 2!")
    exit()

x = []
y = []

for i in range(N):
    x_coord = float(input(f"Введите x для точки {i + 1}: "))
    y_coord = float(input(f"Введите y для точки {i + 1}: "))
    x.append(x_coord)
    y.append(y_coord)

max_perimeter = 0
best_triangle = ()

for (i, j, k) in combinations(range(N), 3):
   
    side1 = distance(x[i], y[i], x[j], y[j])
    side2 = distance(x[j], y[j], x[k], y[k])
    side3 = distance(x[k], y[k], x[i], y[i])
    
   
    perimeter = side1 + side2 + side3
    
    
    if perimeter > max_perimeter:
        max_perimeter = perimeter
        best_triangle = (i, j, k)

if best_triangle:
    print(f"Наибольший периметр треугольника: {max_perimeter:.2f}")
    print("Точки, образующие треугольник:")
    print(f"1: ({x[best_triangle[0]]}, {y[best_triangle[0]]})")
    print(f"2: ({x[best_triangle[1]]}, {y[best_triangle[1]]})")
    print(f"3: ({x[best_triangle[2]]}, {y[best_triangle[2]]})")
else:
    print("Нет треугольников, которые можно сформировать из предоставленных точек.")
