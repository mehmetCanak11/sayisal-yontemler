

#6*x1-2*x2+x3=11
#x1+2*x2-5*x3=-1
#-2*x1+7*x2+2*x3=5
x1=0
x2=0
x3=0

while True:
    x_1,x_2,x_3=x1,x2,x3
    x1=11/6+1/3*x2-1/6*x3
    x2=5/7+2/7*x1-2/7*x3
    x3=1/5+1/5*x1+2/5*x2

    hata=abs(x1-x_1)*abs(x2-x_2)*abs(x3-x_3)

    if(abs(hata)<0.005):
        print("x1=  ",x1,"   x2=  ",x2,"   x3=  ",x3,"    hata=  ",hata)
        break
    print("x1=  ", x1, "   x2=  ", x2, "   x3=  ", x3, "    hata=  ", hata)