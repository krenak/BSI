a = float(input())
b = float(input())
c = float(input())

if a >= b + c or b >= a + c or c >= a + b:
  print("NAO EH TRIANGULO")
elif a == b and b == c:
  print("EQUILATERO")
elif a != b and a != c and b != c:
  print("ESCALENO")
else:
  print("ISOSCELES")
