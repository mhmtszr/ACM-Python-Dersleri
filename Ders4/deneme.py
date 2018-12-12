"""
def isprime(a):
    for i in range(2,(int(a**(1/2))+1)):
        if(a%i==0):
            return False
    return True
a=int(input("Bir sayi giriniz:"))
toplam=0
sayi=0
for i in range(2,a):
    if(isprime(i)==True):
        toplam+=i
        sayi+=1
print(toplam/sayi)
"""
"""
def kare(a):
    return a*a
sayi=5
sayininkaresi=kare(5)
print(sayininkaresi)
"""
"""
a=[1,2,3,4,5]
b=a #b=[1,2,3,4,5]
b.append(10) #b=[1,2,3,4,5,10]
print(a)
c=a[:]
"""
"""
#print(0.1+0.1+0.1-0.3)
"""
"""
a={}
"""
"""
siniflistesi=["Mehmet","Güney","acm"]
notlar=[10,100,50]
"""
"""
a={"Mehmet":10,"Güney":100,"Acm":50}
print(a["Mehmet"])
"""
"""
a.keys() -> keyleri döndürür

a.values() -> valueleri döndürür liste şeklinde

"""
"""
a={"Mehmet":10,"Güney":100,"Acm":50}
print(a.keys())
print(a.values())
"""
"""
dosya=open("output.txt","w") #write
dosya.write("Python dersine hoşgeldiniz")
"""
"""
dosya=open("output.txt","w")
dosya.write("Python\nJava\nC\nC++\n")
"""
dosya=open("output.txt","a") #append
dosya.write("\nHaskell")
"""
dosya=open("output.txt","r") #read
print(dosya.read())
"""
"""
dosya=open("output.txt","w") #önce siler sonra yazar
dosya.write("Güzel programlama dilleridir.")
"""
"""
dosya=open("output.txt","a")
dosya.write("Güzel programlama dilleridir.")
"""
"""
dosya=open("output.txt","r")
a=dosya.readlines()
print(a)
"""
"""
siniflistesi={}
dosya=open("output.txt","r")
a=dosya.readlines()
#mehmet,100
for i in range(len(a)):
    eleman=a[i].strip().split(",")
    siniflistesi[eleman[0]]=eleman[1]
print(siniflistesi)
"""
"""
dosya=open("output.txt","r")
a=dosya.readlines()
print(a)
"""
"""
try:
    print(5/0)
except ZeroDivisionError:
    print("Sayıyı 0 a böldünüz")
"""
"""
try:
    dosya=open("merhaba.txt","r")
    print(dosya.read())
except:
    print("bir hata aldınız")
    
"""
"""
try:
    dosya=open("merhaba.txt","r")
    a=dosya.readlines()
    print(a)
except:
    print("Dosya bulunamadı...")
"""
"""
try:
    a=[0,1,2,3,4,5]
    dosya=open("merhaba.txt","r")
    a=dosya.readlines()
except IndexError:
    print("Index Error")
except ZeroDivisionError:
    print("Sıfıra böldün")
except:
    print("Başka tür bir şeyler oluyor.")
"""
"""
try:
    a=[0,1,2,3,4,5]
    print(a)
except IndexError:
    print("Index Error")
except ZeroDivisionError:
    print("Sıfıra böldün")
else:
    print("sorun yok")
"""
"""
try:
    print(a[3]/a[0])
    a=[0,1,2,3,4,5]
except IndexError:
    print("Index Error")
except ZeroDivisionError:
    print("Sıfıra böldün")
finally:
    print("ACM HACETTEPE")
"""





