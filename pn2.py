import math
def bask(a,b,c):
    delta=(b**2)-4*a*c
    if delta<0:
        return "delta negativo"
    x1=(-b+math.sqrt(delta))/(2*a)
    x2=(-b-math.sqrt(delta))/(2*a)
    return f"x1={x1} e x2={x2}"
print(bask(1,2,1))

