# TODO Найдите количество книг, которое можно разместить на дискете
V = 1.44
l = 100
s = 50
a = 25
b = 4
n = int(V*1024*1024/(l*s*a*b))
print("Количество книг, помещающихся на дискету:", n)
