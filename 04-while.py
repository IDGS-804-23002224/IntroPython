"""x=0
tem=""
while x<10:
    tem+=str(x) + '+'
    x+=2

print("la suma de los numeros pares menores a 10 es")
print(tem)
"""
""" operacion de multiplicacion de a x b utilizando sumas
a=3
b=4
salida: 3+3+3+3 = 12"""

a = 3
b = 4
count = ""
result = 0
i = 0

while i < b:
    count += str(a) + "+"
    result += a
    i+=1

print(count,result)
