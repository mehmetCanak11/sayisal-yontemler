import math
def f(x):
    return (math.e**(-3*x)-x**2)    #(x**2-2*x-3)

x1=0.4  #x1=int(input("birinci degeri giriniz")) #0.4
x2=0.5  #x2=int(input("ikinci degeri giriniz"))

print("++++++++++++",f(x1)) #0.14119421191220205
print("++++++++++++",f(x2)) #-0.026869839851570154
for i in range (2):
    x3=x1-((x2-x1)/(f(x2)-f(x1)))*f(x1)
    hata=(x3-x2)
    #if(abs(hata)<0.003):
     #   print(i,". denemede hata oranı 0.003 den kucuktur")
      #  print("yaklasık deger : ",x3, "hata: ",hata)
        #break
    x1, x2 = x2, x3
    print("x1 : ",x1,"   x2:  ",x2,"    x3:  ",x3) # 0.5    x2:   0.4840121432456371   x3:   0.4840121432456371

     #0.4840121432456371    x2:   0.4839075346690575     x3:   0.4839075346690575

    print("hata: ",hata) # -0.015987856754362872  #-0.00010460857657962341