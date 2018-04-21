import math
def f(x):
    return 4*math.e**(-0.5*x)-x

def fi(x):
    return -2*math.e**(-0.5*x)-1

x=int(input("sayiyi girin: "))

while True:
    x1=x-(f(x)/fi(x))
    hata=-(f(x)/fi(x))
    if(abs(hata)<0.005):
        print("aranan kok(x1) :",x1, "  hata: ",hata)
        break
    print("x  =  ",x, "  x1=  ",x1," hata: ",hata)
    x=x1