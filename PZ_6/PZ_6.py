# Дано множество A из N точек (N > 2, точки заданы своими координатами x, у). 
# Найти наибольший периметр треугольника, вершины которого принадлежат различным точкам множества A,
# и сами эти точки (точки выводятся в том же порядке, в котором они перечислены при задании множества A).
# Расстояние R между точками с координатами (x1, y1) и (x2, у2) вычисляется по формуле: R = √(x2 – x1)2 + (у2 – y1)2.
# Для хранения данных о каждом наборе точек следует использовать по два список: первый список для хранения абсцисс, второй — для хранения ординат.
import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def perimeter(x1, y1, x2, y2, x3, y3):
    return distance(x1, y1, x2, y2) + distance(x2, y2, x3, y3) + distance(x3, y3, x1, y1)

def largest_perimeter(points):
    n = len(points)
    max_perim = 0
    best_triangle = None

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                x3, y3 = points[k]
                perim = perimeter(x1, y1, x2, y2, x3, y3)
                
                if perim > max_perim:
                    max_perim = perim
                    best_triangle = (points[i], points[j], points[k])

    return max_perim, best_triangle

if __name__ == "__main__":
    x_coords = [8, 4, 6, 9]
    y_coords = [0, 1, 2, 3]
    
    points = list(zip(x_coords, y_coords))  
    max_perimeter, triangle_points = largest_perimeter(points)
    
    print("Наибольший периметр:", max_perimeter)
    print("Точки треугольника с наибольшим периметром:", triangle_points)
