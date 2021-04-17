from math import sqrt
def area(a,b,c):
  p=(a+b+c)/2
  A=sqrt(p*(p-a)*(p-b)*(p-c))
  return A
