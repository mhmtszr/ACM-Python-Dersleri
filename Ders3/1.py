"""
print("Hesap makinesi uygulamamiza hosgeldiniz")
while(True):
    print("1-Toplama\n2-Çikarma\n3-Cikis")
    islem=int(input("Lütfen bir islem giriniz"))
    if(islem==1):
        a=int(input("sayi 1:"))
        b=int(input("sayi 2:"))
        print(a+b)
        continue
    elif(islem==2):
        a=int(input("sayi 1:"))
        b=int(input("sayi 2:"))
        print(a-b)
        continue
    else:
        break
"""
"""
a=1
b="1"
if(a==b):
    print("a ve b esit")
else:
    print("a ve b esit degil")
"""
"""
a=int(input("Tahmin edilecek sayiyi giriniz"))
while(True):
    b=int(input("Sizce bu sayi kac: "))
    if(a>b):
        print("Sayiniz istenilen degerden daha kücük")
        continue
    
    elif(a<b):
        print("Sayiniz istenilen degerden daha büyük")
        continue
    elif(a==b):
        print("bildiniz")
        break
"""
"""
a=[1,2,3,4,5]
print(a[0])
"""
"""
a=[1,2,3,4,5]
for i in a:
    print(i)
"""
"""
a=[1,2,3,4,5]
#b=["1","2","3"]
for i in a:
    if(i==3):
        continue
    print(i)
"""
"""
yoklama=["ahmet","ali","ayse"]
a=input("Sinifta mi:?")
for isim in yoklama:
    if(a==isim):
        print("BURDA")
"""
"""
yoklama=["ahmet","ali","ayse"]
a=input("Sinifta mi:?")
b=False
for isim in yoklama:
    if(a==isim):
        print("BURDA")
        b=True
        break
if(b==False):
    print("Burda degil")
"""
"""
yoklama=["ahmet","ali","ayse"]
a=input("Sinifta mi:?") #AHMET
a=a.lower() #ahmet
b=False
for isim in yoklama:
    if(a==isim):
        print("BURDA")
        b=True
        break
if(b==False):
    print("Burda degil")
"""
"""
    .append() --> arraye eleman ekler
    .remove() --> arrayden eleman siler

"""
"""
a=[1,20,3,4,5,6,7,8]
cift=[]
tek=[]
for i in a:
    if(i%2==0):
        cift.append(i)
    else:
        tek.append(i)
print(cift)
print(tek)
"""
"""
a=[-20,-5,3,4,5,-6,7,8,0]
    0   1 2 3  
poz=[]
neg=[]
for i in a:
    if(i<0):
        neg.append(i)
    elif(i>0):
        poz.append(i)
"""
"""
a=3
while(a==3):  #while(True)
    print("Merhaba")
    continue
"""
"""
a="ACM HACETTEPE"
for i in a:
    if(i==" "):
        print("Bosluk var")
"""
"""
while(True):
    parola=input("Bir sifre giriniz:")
    if(len(parola)<3 or len(parola)>7):
        print("Sifreniz 3 den kücük 7 den büyük olamaz")
    else:
        print("Güzel sifre")
        break
"""
"""
def selamla(leee):
    print("Merhaba",leee)

a=input("Isminiz nedir:")
b=input("Isminiz nedir:")
c=input("Isminiz nedir:")
selamla(a) #a=ahmet
selamla(b)
selamla(c)
"""
"""
def selamla(isim,soyisim):
    print("Merhaba",isim,soyisim)

a=input("Isminizi giriniz:")
b=input("Soyisminizi giriniz:")
selamla(a,b)
"""
"""
def topla(array):
    cevap=0
    for i in array:
        cevap+=i
    print("Elemanlarin toplami",cevap)

a=[-10,-2,0,3,4,5,6]
b=[3,4,5,-10]
topla(a)
topla(b)
print(cevap)
"""
"""
def topla(array):
    cevap=0
    for i in array:
        cevap+=i
    return cevap


a=[-10,-2,0,3,4,5,6]
b=[3,4,5,-10]
c=topla(a) #c=6
"""
"""
def topla(array):
    cevap=0
    for i in array:
        cevap+=i
    return cevap
a=[-10,-2,0,3,4,5,6]
cevap=5
c=topla(a)
"""
"""
def yazdir(array,sayi):    
    print(sayi)     

a=[-10,-2,0,3,4,5,6]
cevap=5
yazdir(a,cevap)
"""
"""
def arttir(sayi):
    sayi+=1
    return sayi
sayi=5
sayi=arttir(sayi)
print(sayi)
"""



    

















    






        




    












    











    
