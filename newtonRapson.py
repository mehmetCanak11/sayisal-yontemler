import math
def f(x):
    return (math.e**x)-x**2-2

def fi(x):
    return  math.e**x-2*x

x0=1.3  #x0=int(input("baslangıc noktası giriniz: "))
for i in  range(4):
    x1=x0-(f(x0)/fi(x0))
    hata=x1-x0
    if(abs(hata)<=0.01):
        print("hata oranı 0.01 den kucuktur ", "hata:  ",hata)
        print("yakasık kok : ",x1)
        break
    print("--",x0,"------",x1)
    x0=x1