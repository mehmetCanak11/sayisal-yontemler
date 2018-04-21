

def f(x):
    return(x**2-2*x-3)

x1 = int(input("ilk degere tahminini girin: "))
x2 = int(input("ikinci degere tahminini girin: "))

if(f(x1)*f(x2)==0):
    print("girdiğiniz değerlerden biri denklemin köküdür")
elif(f(x1)*f(x2)>0):
    print("girdiğiniz aralıkta denklemin bir kökü yoktur")
else:
    for i in range(100):
        xr = (x1+x2)/2
        if(f(xr)==0):
            print("çözüm bulundu: ", xr, i)
            break
        elif(f(x1)*f(xr)<0):
            x2 = xr
            e=x1-xr
            print(i," --------- ", e)
            if(abs(e)<0.003):
                print(i,". adımda hata 0.003    ",abs(e))
                break

        else:
            x1 = xr
            e=x2-xr
            print(i," --------- ", e)
            if (abs(e) < 0.003):
                print(i, ". adımda hata 0.003    ", abs(e))
                break

        print(xr,"     ",i)
print(xr,"       ",i)
